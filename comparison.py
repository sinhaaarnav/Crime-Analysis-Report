import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
df = pd.read_csv("india-crime.csv")
crimes = ["Assault on women with intent to outrage her modesty","Cruelty by Husband or his Relatives","Dowry Deaths","Importation of Girls","Insult to modesty of Women","Kidnapping and Abduction","Rape"]

states = df["STATE/UT"].unique()
states = list(states)

cr = pd.DataFrame(crimes)

k=0
for i in states:
    print(f'{k}.',i)
    k+=1
s=int(input("Enter State/UT no. as indicated in the list: "))
print(states[s])

mask1=df['STATE/UT']==states[s]

dd=df[mask1]
dd.head(3)

dd=dd.agg({"Assault on women with intent to outrage her modesty":"sum","Cruelty by Husband or his Relatives":"sum","Dowry Deaths":"sum","Importation of Girls":"sum","Insult to modesty of Women":"sum","Kidnapping and Abduction":"sum","Rape":"sum"})
print(dd)
print(sum(dd))