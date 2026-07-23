#imports

import pandas as pd
import os
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# Loading data
df_secom = pd.read_csv('datasets/uci-secom.csv')

cset_url = 'https://raw.githubusercontent.com/georgetown-cset/eto-chip-explorer/main/data/inputs.csv'
df_cset = pd.read_csv(cset_url)

print(df_cset.head())

#Analyzizng first data set (uci-secom)

print("Dataset Shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

Rows & Columns

#Rows represent as wafer and sensors as columns

print(f" Rows wafers): {df_secomd.shape[0]}")
print(f" Columns (sensors): {df_secom.shape[1]}")

print(df_secom.dtypes.value_counts())

#first few rows

print(df_secom.head())

#missing values

missing = df_secomd.insull().sum

if missing.sum() > 0:
    print(f" Total missing values:"{missing.sum()})
    print(f"   Columns with missing data:")
    print(missing[missing > 0])
else:
    print(" No missing data!")