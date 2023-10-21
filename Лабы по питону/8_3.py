import pandas as pd

df = pd.read_csv('titanic.csv')
survived_by_class = df.groupby(['PClass', 'Survived']).size().reset_index(name='count')
print(survived_by_class)