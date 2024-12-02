
import random
import time
import damage_calculator
import pandas as pd

class Pokemon():
    def __init__(self, name, type1, type1_pred, type2):
        self.name = name
        self.type1_pred = type1_pred
        self.type2 = type2
        self.type1 = type1

class Battle():
    def __init__(self, pokemons_df):
        self.pokemons_df = pokemons_df

    def start_battle(self):
        print("\n♫ ♬tiriturituritrutu ♫ ♬ (Musica di battaglia)\n")
        time.sleep(0.5)
        self.enemy_pokemon = self.generate_enemy_pokemon()
        print(f"Appare {self.enemy_pokemon.name} selvatico!\n")
        time.sleep(0.5)
        print("Scegli il Pokemon da utilizzare!\n")
        time.sleep(0.2)
        self.player_pokemon = self.choose_pokemon()
        time.sleep(0.5)
        print(f"Il tuo {self.player_pokemon.name} di tipo {self.player_pokemon.type1_pred}/{self.player_pokemon.type2} attacca {self.enemy_pokemon.name} selvatico di tipo {self.enemy_pokemon.type1_pred}/{self.enemy_pokemon.type2}!")
        if self.enemy_pokemon.type1_pred != self.enemy_pokemon.type1:
            time.sleep(0.5)
            print(f"Cosa? Pensavi che {self.enemy_pokemon.name} fosse di tipo {self.enemy_pokemon.type1}/{self.enemy_pokemon.type2}?\nNon secondo il nostro modello di Deep Learning!!!")
        if self.player_pokemon.type1_pred != self.player_pokemon.type1:
            time.sleep(0.5)
            print(f"Cosa? Pensavi che {self.player_pokemon.name} fosse di tipo {self.player_pokemon.type1}/{self.player_pokemon.type2}?\nNon secondo il nostro modello di Deep Learning!!!")
        
        time.sleep(0.5)
        damage = damage_calculator.damage_between_two_pokemons(self.player_pokemon, self.player_pokemon)
        vittoria = False
        if damage == 0:
            print(f"Non ha effetto su {self.enemy_pokemon.name} avversario!")
        elif damage > 0 and damage < 1:
            print("Non è molto efficace..")
        elif damage == 1:
            print("Danno neutro...")
        elif damage > 1:
            print("È superefficace!")
            vittoria = True

        if vittoria == False:
            print(f"\nHai perso! Il tuo {self.player_pokemon.name} è stato sconfitto!")
        else:
            print(f"\nHai vinto! Il {self.enemy_pokemon.name} selvatico è stato sconfitto!")


    def generate_enemy_pokemon(self):
        random_id = random.randint(0, len(self.pokemons_df) - 1)
        name = self.pokemons_df["name"].iloc[random_id]
        type1 = self.pokemons_df["type1"].iloc[random_id]
        type1_pred = self.pokemons_df["type1_pred"].iloc[random_id]
        type2 = self.pokemons_df["type2"].iloc[random_id]
        return Pokemon(name, type1, type1_pred, type2)
    
    def choose_pokemon(self):
        while True:
            name = input("Digita il nome del Pokemon che vuoi mandare in campo: ")
            if not self.pokemon_exists(name):
                print("Il Pokemon non esiste!")
            else:
                pk_selected = self.pokemons_df[self.pokemons_df["name"] == name]
                type1 = pk_selected["type1"].array[0]
                type1_pred = pk_selected["type1_pred"].array[0]
                type2 = pk_selected["type2"].array[0]
                print('pk_selected',pk_selected)
                print('name',name)
                print('type1',type1)
                print('type1_pred',type1_pred)
                print('type2',type2)
                return Pokemon(name, type1, type1_pred, type2)

    def pokemon_exists(self,name):
        if name in self.pokemons_df["name"].array:
            return True
        else:
            return False
