import pandas as pd
import numpy as np

def create_df(filename):
    name_df = pd.read_csv(filename)
    name_df = modify_df(name_df)
    return name_df

def modify_df(df):
    df["Sex"] = df["Sex"].replace({"male":1, "female":2})
    df["Embarked"] = df["Embarked"].replace({"S":1, "C":2, "Q":3})
    df["Cabin"] = df["Cabin"].fillna(0)
    df["Cabin"] = df["Cabin"].str[0]
    df["Cabin"] = df["Cabin"].replace({"C": 1, "E": 2, "G": 3, "D": 4, "A": 5, "B": 6, "F": 7, "t": 8})
    df.fillna(-0.5, inplace=True)
    return df

dataframe = create_df("train.csv")
print(dataframe.head())