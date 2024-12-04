# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os


from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

import tensorflow as tf
from tensorflow.keras.datasets import mnist # type: ignore
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense, Dropout # type: ignore
from tensorflow.keras.utils import to_categorical # type: ignore
from tensorflow.keras.utils import plot_model # type: ignore


# %% set parameters for training
EPOCHS = 300
batch_size= 32

# %% load data
df = pd.read_csv('Pokemon.csv')

# %% one hot encoding
encoder = OneHotEncoder(sparse_output=False)
onehot = encoder.fit_transform(df[['Type 1', 'Type 2']])
# set column names
column_names = encoder.get_feature_names_out(['Type 1', 'Type 2'])
encoded_df = pd.DataFrame(onehot, columns=column_names)
result = pd.concat([df, encoded_df], axis=1)
nome = result['Name']
df_y = result[['Type 1_Bug', 'Type 1_Dark','Type 1_Dragon', 'Type 1_Electric', 'Type 1_Fairy','Type 1_Fighting', 'Type 1_Fire', 'Type 1_Flying', 'Type 1_Ghost','Type 1_Grass', 'Type 1_Ground', 'Type 1_Ice', 'Type 1_Normal','Type 1_Poison', 'Type 1_Psychic', 'Type 1_Rock', 'Type 1_Steel','Type 1_Water']]


# %% drop unnecessary columns
result.drop(["Type 1", "Type 2", 'Name', 'Total','#','Type 1_Bug', 'Type 1_Dark','Type 1_Dragon', 'Type 1_Electric', 'Type 1_Fairy','Type 1_Fighting', 'Type 1_Fire', 'Type 1_Flying', 'Type 1_Ghost','Type 1_Grass', 'Type 1_Ground', 'Type 1_Ice', 'Type 1_Normal','Type 1_Poison', 'Type 1_Psychic', 'Type 1_Rock', 'Type 1_Steel','Type 1_Water'], axis=1,  inplace=True)

# %% map string values to 0 and 1 in categorical feature
dict_m ={False: 0, True: 1}
result['Legendary'] = result['Legendary'].map(dict_m)

# %% normalize "stats" features
for col in result.columns.values:
    result[col] = result[col]/result[col].max()


# %% save the size of the input and the number of types
size_input = len(result.columns.values)
len_classi = len(df_y.columns.values)


# %% define X and y for the training as np arrays
X  = result.to_numpy()
y = df_y.to_numpy()
X.astype('float')
y.astype('float')


# %% define train and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

train_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))
test_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test))

# %% automatic optimization of parallelization
AUTOTUNE = tf.data.AUTOTUNE 

train_dataset = train_dataset.batch(batch_size).cache().prefetch(buffer_size=AUTOTUNE)
test_dataset = test_dataset.batch(batch_size).cache().prefetch(buffer_size=AUTOTUNE)


# %% define neural network model
def create_model(units=256):
    model = Sequential()
    model.add(Dense(units*2, activation='relu', input_shape=(size_input,)))
    model.add(Dropout(0.3))
    model.add(Dense(units, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(len_classi, activation='softmax'))
    return model
model = create_model()

# %% compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(0.0001),loss='categorical_crossentropy',
              metrics=['accuracy'] )

# %%
#model.summary()

# %% plot diagram of the model
plot_model(
    model,
    to_file='images/model_architecture.png',  # Percorso del file
    show_shapes=True,                 # Mostra le dimensioni dei tensori
    show_layer_names=True,            # Mostra i nomi dei layer
    rankdir='TB'                      # 'TB' per top-bottom, 'LR' per left-right
)

# %% define checkpoints for the model
checkpoint_path = "model/pokemon_model.keras"
checkpoint_dir = os.path.dirname(checkpoint_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
    monitor='val_loss',       # Metrica da monitorare
    save_best_only=True,      # Salva solo se il modello è migliorato
    save_weights_only=False,  # Salva l'intero modello (architettura + pesi)
    mode='min',               # Salva il modello se la metrica monitorata diminuisce
    verbose=1  )

# %% fit the model
history = model.fit(train_dataset, epochs=EPOCHS,
                      validation_data=test_dataset,
                      callbacks=[cp_callback])

# %% plot the accuracy and loss of the model at each epoch
def plot_history(history):
    key = list(history.history.keys())
    plt.figure(1, figsize=(16,9))
    plt.subplot(1, 2, 1)
    plt.plot(history.history[key[0]])
    plt.plot(history.history[key[2]])
    plt.title("Comparazione "+ str(key[0]))
    plt.legend([key[0], key[2]])
    plt.xlabel("epochs")
    plt.ylabel(str(key[0]))

    # Creare la seconda figura
    plt.subplot(1, 2, 2)
    plt.plot(history.history[key[1]])
    plt.plot(history.history[key[3]])
    plt.title("Comparazione "+ str(key[1]))
    plt.legend([key[1], key[3]])
    plt.xlabel("epochs")
    plt.ylabel(str(key[1]))
    
    plt.savefig('images/'+str(key[0])+'_'+str(key[1])+'.png')

plot_history(history)

# %% make prediction and evaluate the accuracy
predictions = model.predict(X_test)
print(predictions[0])
print(df_y.columns.values[np.argmax(predictions[0], axis=0)])
predicted_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test, axis=1)

predictions = model.predict(X_test)


best_model = tf.keras.models.load_model('model/pokemon_model.keras')
results_evaluate= best_model.evaluate(X_test, y_test)
res_dict = dict(zip(best_model.metrics_names, results_evaluate))
for res in res_dict:
    print(f"{res}: {res_dict[res]}")





