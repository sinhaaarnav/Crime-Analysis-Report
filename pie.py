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

k = 0
for i in states:
    print(f'{k}.', i)
    k +=1
s = int(input("Enter State/UT no. as indicated in the list: "))
print(states[s])
year = int(input("Enter year: "))
print("Year:", year)

mask1 =df['STATE/UT']== states[s]
mask2 =df['Year']== year
dd =df[mask1 & mask2]
dd.head(3)

dd=dd.agg({"Assault on women with intent to outrage her modesty":"sum","Cruelty by Husband or his Relatives":"sum","Dowry Deaths":"sum","Importation of Girls":"sum","Insult to modesty of Women":"sum","Kidnapping and Abduction":"sum","Rape":"sum"})
print(dd)

dd= list(dd)
dd1= pd.Series(dd)
dd1= pd.DataFrame(dd1)

DaTa = pd.concat([cr, dd1], axis=1)
DaTa.columns=["Crime Heads", "Total Crime"]
DaTa=DaTa.set_index("Crime Heads")


plt.style.use('Solarize_Light2')
plt.title(states[s])
DaTa["Total Crime"].plot(kind="pie",labels=None,use_index=False,legend=True,figsize=(10,10))
plt.show()