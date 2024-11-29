import pandas as pd

# Caricamento del dataset (esempio)
# Sostituisci 'file.csv' con il nome del tuo file
df = pd.read_csv('Pokemon.csv')

# Controllo dei valori nulli prima della sostituzione
print("Valori nulli nella colonna 'Other Type of Pokemon' prima della sostituzione:")
print(df['Type 2'].isnull().sum())

# Sostituzione dei valori nulli con la stringa "nessuno"
df['Type 2'] = df['Type 2'].fillna('nessuno')

# Controllo dei valori nulli dopo la sostituzione
print("\nValori nulli nella colonna 'Other Type of Pokemon' dopo la sostituzione:")
print(df['Type 2'].isnull().sum())

# Salvataggio del dataset modificato (opzionale)
df.to_csv('file_modificato.csv', index=False)

# Visualizzazione del risultato (opzionale)
print("\nAnteprima del dataset aggiornato:")
print(df.head())

