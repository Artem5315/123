import pandas as pd

df = pd.read_csv('titanic.csv')
pivot_table = df.pivot_table(index='Sex', columns='PClass', values='Name', aggfunc='count')
survived_by_class = df.groupby(['PClass', 'Survived']).size().reset_index(name='count')
print(pivot_table)
print(survived_by_class)