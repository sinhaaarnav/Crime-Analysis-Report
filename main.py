import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
df = pd.read_csv("india-crime.csv")
crimes = ["Assault on women with intent to outrage her modesty","Cruelty by Husband or his Relatives","Dowry Deaths","Importation of Girls","Insult to modesty of Women","Kidnapping and Abduction","Rape"]

states = df["STATE/UT"].unique()
states = list(states)

sns.heatmap(df.corr(), cmap='Blues', annot=True, fmt='.2f')
plt.figure(figsize=(10, 20))
plt.show()

