import pandas as pd
import numpy as np
from pprint import pprint as pretty
import seaborn as sns


def getDataset():
    
    # On charge le fichier
    dataset = pd.read_csv('default-cards.csv', header=0, sep=';')
    
    # On affecte le bon type à chaque colonnes
    dataset.name = dataset.name.astype(pd.StringDtype())
    dataset.color = dataset.color.astype(pd.StringDtype())
    dataset.cmc = dataset.cmc.astype(pd.Int64Dtype())
    dataset.set = dataset.set.astype(pd.StringDtype())
    dataset.rarity = dataset.rarity.astype(pd.CategoricalDtype(categories=['common', 'uncommon', 'rare', 'mythic'], ordered=True))
    dataset.text = dataset.text.astype(pd.StringDtype())
    dataset.power = dataset.power.astype('float').astype(pd.Int64Dtype())
    dataset.toughness = dataset.toughness.astype('float').astype(pd.Int64Dtype())
    dataset.price_usd = dataset.price_usd.astype('float64')
    dataset.price_eur = dataset.price_eur.astype('float64')
    dataset.type = dataset.type.astype(pd.StringDtype())
    dataset.subtype = dataset.subtype.astype(pd.StringDtype())
    
    return dataset

def explode(df, column, splitter):
    if splitter == '' or splitter == None:
        res = df.drop(column, axis=1).join(df[column].str.join(' ').str.split(expand=True).stack().reset_index(level=1, drop=True).rename(column)).reset_index(drop=True)
    else:
        res = df.drop(column, axis=1).join(df[column].str.split(pat=splitter, expand=True).stack().reset_index(level=1, drop=True).rename(column)).reset_index(drop=True)
    return res[df.columns]