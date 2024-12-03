# PokemonClassifier
![Pokémon Type Classifier](https://github.com/f-lost/PokemonClassifier/blob/main/header.jpg?raw=true "Header")

Progetto di gruppo: Classficazione del tipo di Pokemon a partire dal dataset: https://www.kaggle.com/datasets/abcsds/pokemon

Gruppo: [Alessio Giuseppe Ferraioli](https://github.com/AlessioGFerraioli), [Daniele Florio](https://github.com/DanieleFlo), [Pier Carlo Ciraselli](https://github.com/pierca9494), [Roberta Basile](https://github.com/RobertaBasile), [Stefano Flora](https://github.com/f-lost)

# Classificatore di Tipo Pokemon

## Panoramica
Questo progetto utilizza un modello di **Deep Learning** sviluppato con **TensorFlow** per classificare il tipo di un Pokemon basandosi sulle sue varie caratteristiche. Il modello sfrutta tecniche di apprendimento supervisionato per analizzare e prevedere il tipo di un Pokemon date le sue caratteristiche come statistiche, abilità e altre funzionalità presenti in un dataset popolare sui Pokemon. Inoltre sviluppare parallelamente un gioco tramite il dataset pokemon per creare delle battle in cui la vittoria/sconfitta tra di essa venga decisa dalla tipolagia dei pokemon. Quest'ultima verra pero assegnata dai risultati del nostro modello di DL.

## Caratteristiche
- **Dataset:** Utilizza un dataset contenente info sui Pokemon.
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
├── damage_calculator.py      # Funzioni di calcolo dei danni in battaglia
├── battle.py                 # Simulazione battaglia Pokemon
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
- matplotlib (opzionale, per visualizzazioni)

### Installazione
1. Clona il repository:
   ```bash
   git clone https://github.com/yourusername/pokemon-type-classifier.git
   cd pokemon-type-classifier
   ```
2. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```

### Utilizzo


1. Preprocessa i dati:
   ```bash
   python src/preprocess.py
   ```
2. Allena il modello:
   ```bash
   python main.py
   ```
3. Valuta il modello:
   ```bash
   python src/evaluate.py
   ```

## Architettura del Modello
Il modello è composto dai seguenti livelli:
1. Livello di input per accettare tutte le caratteristiche numeriche e codificate.
2. Diversi livelli nascosti completamente connessi con attivazione ReLU.
3. Livelli di dropout per la regolarizzazione.
4. Livello di output con una funzione di attivazione softmax per prevedere le probabilità per ogni tipo.

## Risultati
Il modello raggiunge un'accuratezza del **X%** sul dataset di test dopo **Y epoche** di allenamento. Metriche aggiuntive come precisione, richiamo e F1-score vengono utilizzate per valutare ulteriormente le prestazioni.


## Ringraziamenti
- Il dataset dei Pokemon è stato ottenuto da [Kaggle](https://www.kaggle.com).
- Un ringraziamento speciale alla comunità TensorFlow per i loro tutorial e documentazione completi.



