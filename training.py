# %%
import matplotlib.pyplot as plt
import os

import tensorflow as tf
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense, Dropout # type: ignore
from tensorflow.keras.utils import plot_model # type: ignore

def training(batch_size=32,
                epochs,
                X_train,
                X_test,
                y_train,
                y_test
                ):
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

    return model
