import pandas as pd
import os
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np


# Loading data
df_secom = pd.read_csv('datasets/uci-secom.csv')

print(df.head())

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