# %%
import numpy as np
import pandas as pd
import os


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

import tensorflow as tf
from tensorflow.keras.utils import to_categorical # type: ignore
from tensorflow.keras.utils import plot_model # type: ignore

def preprocess(filename):

    # %% load data
    df = pd.read_csv(filename)

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


    return X_train, X_test, y_train, y_test
