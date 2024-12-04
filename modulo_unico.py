import pandas as pd
import numpy as np
import random
import time

import tensorflow as tf
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense # type: ignore

from sklearn.preprocessing import OneHotEncoder

import tkinter as tk
from tkinter import simpledialog, messagebox




# Classe Pokémon
class Pokemon:
    def __init__(self, name, type1, type1_pred, type2):
        self.name = name
        self.type1_pred = type1_pred
        self.type2 = type2
        self.type1 = type1


class Battle:
    def __init__(self, pokemons_df):
        self.pokemons_df = pokemons_df
        self.root = tk.Tk()
        self.root.withdraw()  # Nasconde la finestra principale, serve solo per dialoghi

    def show_message(self, message):
        """Mostra un messaggio in una finestra grafica."""
        messagebox.showinfo("Pokémon Battle", message)

    def choose_pokemon(self):
        """Permette di scegliere un Pokémon tramite dialogo grafico."""
        while True:
            name = simpledialog.askstring("Scegli Pokémon", "Digita il nome del Pokémon che vuoi mandare in campo:")
            if not name:
                messagebox.showerror("Errore", "Devi inserire un nome!")
                continue

            if not self.pokemon_exists(name):
                messagebox.showerror("Errore", f"Il Pokémon {name} non esiste!")
            else:
                pk_selected = self.pokemons_df[self.pokemons_df["name"] == name]
                type1 = pk_selected["type1"].iloc[0]
                type1_pred = pk_selected["type1_pred"].iloc[0]
                type2 = pk_selected["type2"].iloc[0]
                return Pokemon(name, type1, type1_pred, type2)

    def pokemon_exists(self, name):
        """Verifica se un Pokémon esiste nel DataFrame."""
        return name in self.pokemons_df["name"].values

    def generate_enemy_pokemon(self):
        """Genera un Pokémon nemico casuale."""
        random_id = random.randint(0, len(self.pokemons_df) - 1)
        name = self.pokemons_df["name"].iloc[random_id]
        type1 = self.pokemons_df["type1"].iloc[random_id]
        type1_pred = self.pokemons_df["type1_pred"].iloc[random_id]
        type2 = self.pokemons_df["type2"].iloc[random_id]
        return Pokemon(name, type1, type1_pred, type2)

    def start_battle(self):
        """Gestisce l'intero flusso della battaglia."""
        self.show_message("♫ ♬tiriturituritrutu ♫ ♬ (Musica di battaglia)")
        time.sleep(0.5)

        self.enemy_pokemon = self.generate_enemy_pokemon()
        self.show_message(f"Appare {self.enemy_pokemon.name} selvatico!")

        self.show_message("Scegli il Pokémon da utilizzare!")
        self.player_pokemon = self.choose_pokemon()

        self.show_message(
            f"Il tuo {self.player_pokemon.name} di tipo {self.player_pokemon.type1_pred}/{self.player_pokemon.type2} "
            f"attacca {self.enemy_pokemon.name} selvatico di tipo {self.enemy_pokemon.type1_pred}/{self.enemy_pokemon.type2}!"
        )

        if self.enemy_pokemon.type1_pred != self.enemy_pokemon.type1:
            self.show_message(
                f"Cosa? Pensavi che {self.enemy_pokemon.name} fosse di tipo {self.enemy_pokemon.type1}/{self.enemy_pokemon.type2}?\n"
                "Non secondo il nostro modello di Deep Learning!"
            )

        if self.player_pokemon.type1_pred != self.player_pokemon.type1:
            self.show_message(
                f"Cosa? Pensavi che {self.player_pokemon.name} fosse di tipo {self.player_pokemon.type1}/{self.player_pokemon.type2}?\n"
                "Non secondo il nostro modello di Deep Learning!"
            )

        damage = damage_between_two_pokemons(self.player_pokemon, self.enemy_pokemon)
        vittoria = False

        if damage == 0:
            self.show_message(f"Non ha effetto su {self.enemy_pokemon.name} avversario!")
        elif 0 < damage < 1:
            self.show_message("Non è molto efficace...")
        elif damage == 1:
            self.show_message("Danno neutro...")
        elif damage > 1:
            self.show_message("È superefficace!")
            vittoria = True

        if not vittoria:
            self.show_message(f"Hai perso! Il tuo {self.player_pokemon.name} è stato sconfitto!")
        else:
            self.show_message(f"Hai vinto! Il {self.enemy_pokemon.name} selvatico è stato sconfitto!")


    def generate_enemy_pokemon(self):
        """Genera un Pokémon avversario casuale."""
        random_id = random.randint(0, len(self.pokemons_df) - 1)
        row = self.pokemons_df.iloc[random_id]
        return Pokemon(row["name"], row["type1"], row["type1_pred"], row["type2"])

    def choose_pokemon(self):
        """Permette di scegliere un Pokémon tramite dialogo grafico."""
        while True:
            name = simpledialog.askstring("Scegli Pokémon", "Digita il nome del Pokémon che vuoi mandare in campo:")
            if not name:
                messagebox.showerror("Errore", "Devi inserire un nome!")
                continue

            if not self.pokemon_exists(name):
                messagebox.showerror("Errore", f"Il Pokémon {name} non esiste!")
            else:
                pk_selected = self.pokemons_df[self.pokemons_df["name"] == name]
                type1 = pk_selected["type1"].iloc[0]
                type1_pred = pk_selected["type1_pred"].iloc[0]
                type2 = pk_selected["type2"].iloc[0]
                return Pokemon(name, type1, type1_pred, type2)

    def pokemon_exists(self, name):
        """Controlla se il Pokémon esiste nel dataset."""
        return name in self.pokemons_df["name"].values

    def display_damage_result(self, damage):
        """Mostra il risultato del danno inflitto."""
        if damage == 0:
            print(f"Non ha effetto su {self.enemy_pokemon.name} avversario!")
        elif damage > 0 and damage < 1:
            print("Non è molto efficace..")
        elif damage == 1:
            print("Danno neutro...")
        else:
            print("È superefficace!")

        if damage > 1:
            print(f"\nHai vinto! Il {self.enemy_pokemon.name} selvatico è stato sconfitto!")
        else:
            print(f"\nHai perso! Il tuo {self.player_pokemon.name} è stato sconfitto!")


#Classe Menu
class Menu:
    def __init__(self):
        self.__elementi = []

    def aggiungi_elemento(self, elemento):
        """Aggiunge un elemento al menu."""
        if isinstance(elemento, Elemento):
            self.__elementi.append(elemento)
        else:
            raise TypeError("L'elemento deve essere un'istanza della classe Elemento")

    def mostra_menu(self):
        """Mostra il menu e gestisce le selezioni."""
        while True:
            print("\nMenu:")
            for i, elemento in enumerate(self.__elementi, start=1):
                print(f"{i}. {elemento.get_nome()}")
            print(f"{len(self.__elementi) + 1}. Esci")

            try:
                scelta = int(input("Seleziona il numero dell'opzione: "))
                if 1 <= scelta <= len(self.__elementi):
                    self.__elementi[scelta - 1].esegui_azione()
                elif scelta == len(self.__elementi) + 1:
                    print("Uscita dal menu.")
                    break
                else:
                    print("Scelta non valida. Riprova.")
            except ValueError:
                print("Per favore, inserisci un numero valido.")


class Elemento:
    def __init__(self, nome, azione=None):
        self.__nome = nome
        self.__azione = azione

    def get_nome(self):
        return self.__nome

    def esegui_azione(self):
        """Esegue l'azione associata."""
        if self.__azione:
            self.__azione.esegui()
        else:
            print(f"{self.__nome} non ha alcuna azione associata.")


class Azione:
    def __init__(self, funzione):
        self.__funzione = funzione

    def esegui(self):
        """Esegue la funzione associata."""
        if callable(self.__funzione):
            self.__funzione()
        else:
            raise ValueError("L'azione deve essere una funzione chiamabile")


#dizionario per gestire i danni tra tipi
damage_received = {
    'Normal':{'Fighting':2., 'Ghost':0.},
    'Fire':{
            'Fire':0.5,
            'Water':2,
            'Grass':0.5,
            'Ice':0.5,
            'Ground':2,
            'Bug':0.5,
            'Rock': 2,
            'Steel': 0.5,
            'Fairy': 0.5
    },
    'Water':{
            'Fire':0.5,
            'Water':0.5,
            'Electric': 2,
            'Grass':2,
            'Ice':0.5,
            'Ground':2,
            'Bug':0.5,
            'Rock': 2,
            'Steel': 0.5,
            'Fairy': 0.5
    },        
    'Electric':{
            'Electric': 0.5,
            'Ground':2,
            'Flying':.5,
            'Steel': 0.5,
    },
    'Grass':{
            'Fire':2,
            'Water':0.5,
            'Electric': 0.5,
            'Grass':0.5,
            'Ice':2,
            'Poison':2,
            'Ground':0.5,
            'Flying':2,
            'Bug':2,
    },
    'Ice':{
            'Fire':2,
            'Ice':0.5,
            'Fighting':2,
            'Poison':2,
            'Ground':.5,
            'Flying':2,
            'Bug':2,
    } ,
    'Fighting':{
            'Flying':2,
            'Psychic':2,
            'Bug':.5,
            'Rock':.5,
            'Dark': .5,
            'Steel': 2,
    },
    'Poison':{
            'Grass':0.5,
            'Fighting':0.5,
            'Poison':0.5,
            'Ground':2,
            'Psychic':2,
            'Bug':0.5,
            'Fairy': 0.5
    },
    'Ground':{
            'Water':2,
            'Electric': 0,
            'Grass':2,
            'Ice':2,
            'Fighting':1,
            'Poison':0.5,
            'Ground':0.5,
            'Flying':1,
            'Psychic':1,
            'Bug':1,
            'Rock':0.5,
            'Ghost':1,
            'Dragon':1,
            'Dark': 0.5,
            'Steel': 1,
            'Fairy': 2
    },
    'Flying':{
            'Electric': 2,
            'Grass':0.5,
            'Ice':2,
            'Fighting':0.5,
            'Poison':1,
            'Ground':0,
            'Flying':1,
            'Psychic':1,
            'Bug':0.5,
    },
    'Psychic':{
            'Fighting':.5,
            'Psychic':.5,
            'Bug':2,
            'Ghost':2,
            'Dragon':1,
            'Dark': 2,
            'Steel': 1,
            'Fairy': 1
    },
    'Bug':{
            'Fire':2,
            'Grass':0.5,
            'Ice':1,
            'Fighting':0.5,
            'Poison':1,
            'Ground':0.5,
            'Flying':2,
            'Psychic':1,
            'Bug':1,
            'Rock':2,
    },
    'Rock':{
            'Normal':0.5,
            'Fire':0.5,
            'Water':2,
            'Electric': 1,
            'Grass':2,
            'Ice':1,
            'Fighting':2,
            'Poison':0.5,
            'Ground':2,
            'Flying':0.5,
    },
    "Ghost":{            
            'Normal':0,
            'Fighting':0,
            'Poison':0.5,
            'Ground':1,
            'Flying':1,
            'Psychic':1,
            'Bug':0.5,
            'Rock':1,
            'Ghost':2,
            'Dragon':1,
            'Dark': 2,
            'Steel': 1,
            'Fairy': 1
    },
    'Dragon':{
            'Fire':0.5,
            'Water':0.5,
            'Electric': 0.5,
            'Grass':0.5,
            'Ice':2,
            'Dragon':2,
            'Dark': 1,
            'Steel': 1,
            'Fairy': 2
    },
    'Dark':{
            'Fighting':2,
            'Psychic':0,
            'Bug':2,
            'Rock':1,
            'Ghost':0.5,
            'Dragon':1,
            'Dark': 0.5,
            'Steel': 1,
            'Fairy': 0.5
    },
    "Steel":{
            'Normal':0.5,
            'Fire':2,
            'Water':1,
            'Electric': 1,
            'Grass':0.5,
            'Ice':0.5,
            'Fighting':2,
            'Poison':0,
            'Ground':2,
            'Flying':0.5,
            'Psychic':0.5,
            'Bug':0.5,
            'Rock':0.5,
            'Ghost':1,
            'Dragon':0.5,
            'Dark': 1,
            'Steel': 0.5,
            'Fairy': 0.5
    },
    "Fairy":{
            'Fighting':0.5,
            'Poison':2,
            'Bug':0.5,
            'Dragon':0,
            'Dark': 0.5,
            'Steel': 2,
            'Fairy': 1
    },
    'Nessuno':{}
}



# Funzioni di calcolo danni
def binary_damage_calculation(atk_type, def_type):
    """Calcola il danno tra un tipo attaccante e un tipo difensivo."""
    if atk_type in damage_received[def_type].keys():
        return damage_received[def_type][atk_type]
    return 1.0


def damage_double_typing(atk_types, def_types):
    """Calcola il danno totale tra due Pokémon con tipi doppi."""
    damage = 1
    for atk_type in atk_types:
        for def_type in def_types:
            damage *= binary_damage_calculation(atk_type, def_type)
    return damage


def damage_between_two_pokemons(atk_pokemon, def_pokemon):
    """Calcola il danno tra due Pokémon."""
    atk_types = [atk_pokemon.type1_pred, atk_pokemon.type2]
    def_types = [def_pokemon.type1_pred, def_pokemon.type2]
    return damage_double_typing(atk_types, def_types)

#Funzioni caricamento e pulizia del dataset e caricamento modello
def load_model():
    # Carico i pesi del modello
    model_path = "model/pokemon_model.keras"
    model = tf.keras.models.load_model(model_path)
    return model

def load_dataset():
    """Carica e pre-elabora il dataset di Pokémon."""
    # Legge il file CSV e gestisce valori mancanti
    df = pd.read_csv('Pokemon.csv')
    df.fillna('Nessuno', inplace=True)

    # One-hot encoding per i tipi dei Pokémon
    encoder = OneHotEncoder(sparse_output=False)
    onehot = encoder.fit_transform(df[['Type 1', 'Type 2']])
    column_names = encoder.get_feature_names_out(['Type 1', 'Type 2'])
    encoded_df = pd.DataFrame(onehot, columns=column_names)

    # Unisce il dataset originale con l'encoding
    result = pd.concat([df, encoded_df], axis=1)

    # Estrae i nomi dei Pokémon e le colonne target
    nome = result['Name']
    df_y = result[[
        'Type 1_Bug', 'Type 1_Dark', 'Type 1_Dragon', 'Type 1_Electric',
        'Type 1_Fairy', 'Type 1_Fighting', 'Type 1_Fire', 'Type 1_Flying',
        'Type 1_Ghost', 'Type 1_Grass', 'Type 1_Ground', 'Type 1_Ice',
        'Type 1_Normal', 'Type 1_Poison', 'Type 1_Psychic', 'Type 1_Rock',
        'Type 1_Steel', 'Type 1_Water'
    ]]

    # Rimuove colonne inutili dal dataset
    result.drop(
        [
            "Type 1", "Type 2", 'Name', 'Total', '#',
            'Type 1_Bug', 'Type 1_Dark', 'Type 1_Dragon', 'Type 1_Electric',
            'Type 1_Fairy', 'Type 1_Fighting', 'Type 1_Fire', 'Type 1_Flying',
            'Type 1_Ghost', 'Type 1_Grass', 'Type 1_Ground', 'Type 1_Ice',
            'Type 1_Normal', 'Type 1_Poison', 'Type 1_Psychic', 'Type 1_Rock',
            'Type 1_Steel', 'Type 1_Water'
        ],
        axis=1,
        inplace=True
    )

    # Mappa il campo "Legendary" in valori numerici
    dict_m = {False: 0, True: 1}
    result['Legendary'] = result['Legendary'].map(dict_m)

    # Normalizza i valori numerici
    for col in result.columns.values:
        result[col] = result[col] / result[col].max()

    # Converte il dataset in una matrice numerica
    X = result.to_numpy()
    X = X.astype('float')

    # Carica il modello di deep learning
    model = load_model()

    # Predice i tipi dei Pokémon
    data = tf.constant(X)
    res = model.predict(data, verbose=0)

    # Determina il tipo predetto
    tot_res = []
    for r in res:
        tot_res.append(df_y.columns.values[np.argmax(r, axis=0)][7:])

    # Costruisce il dataset finale
    dict_tot = {
        'name': nome,
        'type1': df['Type 1'],
        'type1_pred': tot_res,
        'type2': df['Type 2'],
    }
    df_tot = pd.DataFrame(dict_tot)

    return df_tot

#Funzioni richiamate nel menù
def gioca():
    df = load_dataset()
    battle = Battle(df)
    while True:
        # Avvia la battaglia e mostra i risultati
        battle.start_battle()
        risposta = messagebox.askyesno("Continua", "Vuoi continuare a giocare?")
        if not risposta:
            break

def ringraziamenti():
    messagebox.showinfo("Ringraziamenti", "Grazie per aver giocato!\nCredits: Alessio, Daniele, Pier Carlo, Roberta, Stefano")


