import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('india-crime.csv')
df.tail()

df_mh = df[df['STATE/UT'] == 'Maharashtra']
df_mh1 = df_mh.loc[df_mh['DISTRICT'] == 'RAIGAD']

top = df_mh1.loc['Kidnapping and Abduction'].sum()
print(top)

