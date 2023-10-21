import pandas as pd

df = pd.read_csv('titanic.csv')
print(df)
print(df.groupby('Survived').agg({'SexCode':['count']}))#2
print()
print(df.groupby('PClass').agg({'SexCode':['count']}))#3
print()
print(df.pivot_table(index= 'SexCode', columns= 'PClass', aggfunc='count', margins= False))