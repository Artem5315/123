import pandas as pd

# Загрузка данных из файла
data = pd.read_csv('titanic.csv')

# Группировка данных по полу и статусу выживания
grouped_data = data.groupby(['Sex', 'Survived']).size().reset_index(name='Count')

# Фильтрация данных для получения количества выживших и погибших женщин и мужчин
survived_female = grouped_data[(grouped_data['Sex'] == 'female') & (grouped_data['Survived'] == 1)]['Count'].values[0]
died_female = grouped_data[(grouped_data['Sex'] == 'female') & (grouped_data['Survived'] == 0)]['Count'].values[0]
survived_male = grouped_data[(grouped_data['Sex'] == 'male') & (grouped_data['Survived'] == 1)]['Count'].values[0]
died_male = grouped_data[(grouped_data['Sex'] == 'male') & (grouped_data['Survived'] == 0)]['Count'].values[0]

# Вывод результатов
print(f"Выжило женщин: {survived_female}")
print(f"Погибло женщин: {died_female}")
print(f"Выжило мужчин: {survived_male}")
print(f"Погибло мужчин: {died_male}")
