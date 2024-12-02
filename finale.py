from modulo_menu import Menu, Elemento, Azione
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

import tensorflow as tf
from tensorflow.keras.datasets import mnist # type: ignore
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense, Flatten # type: ignore
from tensorflow.keras.utils import to_categorical # type: ignore


df = pd.read_csv('Pokemon.csv')
checkpoint_path = "model/pokemon_model.weights.h5"
checkpoint_dir = os.path.dirname(checkpoint_path)
model2 = Sequential()
model2.add(Dense(256, activation='relu', input_shape=(size_input,)))
model2.add(Dense(128, activation='relu'))
model2.add(Dense(len_classi, activation='softmax'))
model2.load_weights(checkpoint_path)
predictions = model2.predict(X_test)
print(predictions[0])
print(df_y.columns.values[np.argmax(predictions[0], axis=0)])
predicted_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test, axis=1)

predictions = model2.predict(X_test)






def ringrazia():
    






# Creazione del menu e aggiunta degli elementi
menu = Menu()



elemento1 = Elemento("Gioca", Azione(numero))
elemento2 = Elemento("Addio", Azione(equazione))
elemento3 = Elemento("Ringraziamenti", Azione(ringrazia))

menu.aggiungi_elemento(elemento1)
menu.aggiungi_elemento(elemento2)
menu.aggiungi_elemento(elemento3)

# Mostra il menu ripetibile
menu.mostra_menu()