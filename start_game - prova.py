import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from modulo_menu import Menu, Azione, Elemento
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from battle import Battle, Pokemon

import tensorflow as tf
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense # type: ignore

def load_model():
    # Carico i pesi del modello
    model_path = "model/pokemon_model.h5"
    model = tf.keras.models.load_model(model_path)
    return model

def load_dataset():
    df = pd.read_csv('Pokemon.csv')
    df.fillna('Nessuno', inplace=True)
    encoder = OneHotEncoder(sparse_output=False)
    onehot = encoder.fit_transform(df[['Type 1', 'Type 2']])
    column_names = encoder.get_feature_names_out(['Type 1', 'Type 2'])
    encoded_df = pd.DataFrame(onehot, columns=column_names)
    result = pd.concat([df, encoded_df], axis=1)
    nome = result['Name']
    df_y = result[['Type 1_Bug', 'Type 1_Dark','Type 1_Dragon', 'Type 1_Electric', 'Type 1_Fairy','Type 1_Fighting', 'Type 1_Fire', 'Type 1_Flying', 'Type 1_Ghost','Type 1_Grass', 'Type 1_Ground', 'Type 1_Ice', 'Type 1_Normal','Type 1_Poison', 'Type 1_Psychic', 'Type 1_Rock', 'Type 1_Steel','Type 1_Water']]
    result.drop(["Type 1", "Type 2", 'Name', 'Total','#','Type 1_Bug', 'Type 1_Dark','Type 1_Dragon', 'Type 1_Electric', 'Type 1_Fairy','Type 1_Fighting', 'Type 1_Fire', 'Type 1_Flying', 'Type 1_Ghost','Type 1_Grass', 'Type 1_Ground', 'Type 1_Ice', 'Type 1_Normal','Type 1_Poison', 'Type 1_Psychic', 'Type 1_Rock', 'Type 1_Steel','Type 1_Water'], axis=1,  inplace=True)
    dict_m ={False: 0, True: 1}
    result['Legendary'] = result['Legendary'].map(dict_m)
    for col in result.columns.values:
        result[col] = result[col]/result[col].max()
    X  = result.to_numpy()

    X.astype('float')
    model = load_model()
    data = tf.constant(X)
    res = model.predict(data, verbose=0)
    tot_res = []
    for r in res:
        tot_res.append(df_y.columns.values[np.argmax(r, axis=0)][7:])
    
    dict_tot = {
        'name': nome,
        'type1': df['Type 1'],
        'type1_pred': tot_res,
        'type2': df['Type 2'],
        
    }
    df_tot = pd.DataFrame(dict_tot)
    return df_tot

def gioca():
    df = load_dataset()
    battle  = Battle(df)
    while True:
        battle.start_battle()
        nav = input('Vuoi continuare a giocare? (yes/no)')
        if nav == 'no' or nav=='n':
            break

def ringraziamenti():
    messagebox.showinfo("Ringraziamenti", "Grazie per aver giocato\nCredit: Stefano, Alessio, Roberta, Pier Carlo, Daniele")

def mostra_menu():
    root = tk.Tk()
    root.title("Menu Pokémon")
    root.geometry("600x400")

    # Caricamento dell'immagine di sfondo
    bg_image = ImageTk.PhotoImage(Image.open("sfondo.jpg"))
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    btn_gioca = tk.Button(root, text="Gioca", command=gioca)
    btn_gioca_window = canvas.create_window(300, 150, window=btn_gioca)

    btn_ringraziamenti = tk.Button(root, text="Ringraziamenti", command=ringraziamenti)
    btn_ringraziamenti_window = canvas.create_window(300, 200, window=btn_ringraziamenti)

    btn_esci = tk.Button(root, text="Esci", command=root.destroy)
    btn_esci_window = canvas.create_window(300, 250, window=btn_esci)

    root.mainloop()

menu = Menu()

elemento1 = Elemento("Gioca", Azione(gioca))
elemento3 = Elemento("Ringraziamenti", Azione(ringraziamenti))

menu.aggiungi_elemento(elemento1)
menu.aggiungi_elemento(elemento3)

# Mostra il menu grafico
mostra_menu()

