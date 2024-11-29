# PokemonClassifier

Progetto di gruppo: Classficazione del tipo di Pokemon a partire dal dataset: https://www.kaggle.com/datasets/abcsds/pokemon

Gruppo: Alessio Ferraioli, Daniele Florio, Pier Carlo Ciraselli, Roberta Basile, Stefano Flora

# Classificatore di Tipo Pokemon

## Panoramica
Questo progetto utilizza un modello di **Deep Learning** sviluppato con **TensorFlow** per classificare il tipo di un Pokemon basandosi sulle sue varie caratteristiche. Il modello sfrutta tecniche di apprendimento supervisionato per analizzare e prevedere il tipo di un Pokemon date le sue caratteristiche come statistiche, abilità e altre funzionalità presenti in un dataset popolare sui Pokemon. Inoltre sviluppare parallelamente un gioco tramite il dataset pokemon per creare delle battle in cui la vittoria/sconfitta tra di essa venga decisa dalla tipolagia dei pokemon. Quest'ultima verra pero assegnata dai risultati del nostro modello di DL.

## Caratteristiche
- **Dataset:** Utilizza un dataset completo sui Pokemon.
- **Framework di Deep Learning:** TensorFlow.
- **Obiettivo:** Predire il tipo (o i tipi) di un Pokemon (es. Fuoco, Acqua, Erba) basandosi sulle sue caratteristiche.
- **Preprocessing dei Dati:** Gestisce valori mancanti, normalizza le caratteristiche e codifica le variabili categoriali.
- **Architettura del Modello:** Implementa una rete neurale con livelli nascosti progettati per ottenere un'elevata accuratezza nella classificazione.

## Dataset
Il dataset contiene informazioni su diversi Pokemon, tra cui:
- Statistiche di HP, Attacco, Difesa, Attacco Speciale, Difesa Speciale e Velocità.
- Abilità.
- Generazione.
- Stato di leggendario.
- E altro ancora.

Il dataset deve essere preprocessato per:
1. Gestire i valori mancanti (es. riempire o rimuovere voci con dati incompleti).
2. Normalizzare le caratteristiche numeriche.
3. Codificare le variabili categoriali (es. abilità) tramite one-hot encoding.

## Struttura del Progetto
```
Pokemon-Type-Classifier/
├── data/                # File del dataset
├── notebooks/           # Jupyter notebook per EDA e prototipazione
├── models/              # Modelli salvati e checkpoint
├── src/                 # Codice sorgente
│   ├── preprocess.py    # Pipeline di preprocessing dei dati
│   ├── model.py         # Architettura del modello e codice di training
│   ├── evaluate.py      # Metriche di valutazione e test
├── requirements.txt     # Dipendenze Python
├── README.md            # Descrizione del progetto (questo file)
└── main.py              # Punto di ingresso per eseguire la pipeline di training
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

## Licenza
Questo progetto è concesso in licenza sotto la licenza MIT. Consulta il file `LICENSE` per i dettagli.


