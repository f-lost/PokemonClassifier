# PokemonClassifier
![Pokémon Type Classifier](https://github.com/f-lost/PokemonClassifier/blob/main/header.jpg?raw=true "Header")

Progetto di gruppo: Classficazione del tipo di Pokemon a partire dal dataset: https://www.kaggle.com/datasets/abcsds/pokemon

Gruppo: [Alessio Giuseppe Ferraioli](https://github.com/AlessioGFerraioli), [Daniele Florio](https://github.com/DanieleFlo), [Pier Carlo Ciraselli](https://github.com/pierca9494), [Roberta Basile](https://github.com/RobertaBasile), [Stefano Flora](https://github.com/f-lost)

# Classificatore di Tipo Pokemon

## Panoramica
Questo progetto utilizza un modello di **Deep Learning** sviluppato con **TensorFlow** per classificare il tipo di un Pokemon basandosi sulle sue varie caratteristiche. Il modello sfrutta tecniche di apprendimento supervisionato per **prevedere** il **tipo di un Pokemon** date le sue caratteristiche presenti in un dataset popolare sui Pokemon. Inoltre, include un **mini-gioco** che simula delle **battaglie Pokemon** in cui la vittoria/sconfitta tra di essa dipende dalle interazioni tra i tipi dei Pokemon. *Ma attenzione!* Il tipo del Pokemon è quello assegnato dal nostro modello di DL!

## Caratteristiche
- **Dataset:** Utilizza un dataset contenente info basilari sui Pokemon.
- **Framework di Deep Learning:** TensorFlow.
- **Obiettivo:** Predire il tipo principale di un Pokemon (es. Fire, Water, Grass) basandosi sulle sue caratteristiche.
- **Mini-Game:** Permettere all'utente di giocare una versione semplificata di una battaglia Pokemon, in cui il tipo dei Pokemon è quello generato dal modello. 
- **Preprocessing dei Dati:** Normalizza le caratteristiche e codifica le variabili categoriali.
- **Architettura del Modello:** Implementa una rete neurale con livelli nascosti progettati per ottenere una migliore  accuratezza nella classificazione.

## Dataset
Il dataset contiene informazioni su diversi Pokemon, tra cui:
- Nome
- statistiche di HP, Attacco, Difesa, Attacco Speciale, Difesa Speciale e Velocità;
- tipo principale;
- tipo secondario;
- se è leggendario o no;
- e altro ancora

Il dataset deve essere preprocessato per:
1. Normalizzare le caratteristiche numeriche.
2. Codificare le variabili categoriali (es. tipi del Pokemon) tramite one-hot encoding.

## Struttura del Progetto
```
Pokemon-Classifier/
├── model/                    # File del modello
├── modulo_unico.py           # Contiene tutte le classi e le funzioni necessarie al gioco
├── genera_modello_DL.ipynb   # Genera modello Deep Learning
├── README.md                 # Descrizione del progetto (questo file)
└── start_game.py             # Inizia il MiniGame battaglia Pokemon

```

## Setup
### Prerequisiti
Assicurati di avere installato Python 3.8 o versioni superiori insieme alle seguenti librerie:
- TensorFlow
- NumPy
- pandas
- scikit-learn
- Pillow (il mini-game appare in una finestra grafica)
- matplotlib (opzionale, per visualizzazioni)


## Architettura del Modello
Il modello è composto dai seguenti livelli:
1. Livello di input per accettare tutte le caratteristiche numeriche e codificate.
2. Diversi livelli nascosti completamente connessi con attivazione ReLU.
3. Livelli di dropout per la regolarizzazione.
4. Livello di output con una funzione di attivazione softmax per prevedere le probabilità per ogni tipo.

## Risultati
Il modello raggiunge un'accuratezza del **30%** sul dataset di test dopo **200 epoche** di allenamento. 

Ogni appassionato di Pokemon sa che non c'è un collegamento preciso tra il tipo del Pokemon e le sue statistiche o tipo secondario. Bensì, queste caratteristiche sono decise dai game developer sulla base di motivazioni di **storytelling** e **game design**. Tuttavia, un giocatore attento nota che alcuni **pattern** emergono - *ad esempio, i Pokemon di tipo Steel (Acciaio) hanno solitamente una difesa elevata*. 
Il nostro modello è in grado di carprire alcuni di questi pattern e ottenere una accuracy considerevolmente più alta del random chance, equivalente al **5%**.


## Ringraziamenti
- Il dataset dei Pokemon è stato ottenuto da [Kaggle](https://www.kaggle.com).
- Un ringraziamento speciale alla comunità TensorFlow per i loro tutorial e documentazione completi.



