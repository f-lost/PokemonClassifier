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
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense, Dropout # type: ignore
from tensorflow.keras.utils import to_categorical # type: ignore
from tensorflow.keras.utils import plot_model # type: ignore

def evaluate(model, X_train, X_test, y_train, y_test):
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





