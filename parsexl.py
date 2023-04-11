import pandas as pd
import sqlite3


# Чтение Excel файла и создание датафрейма Pandas
df = pd.read_excel('example.xlsx')
# print(df)

# Подключение к базе данных SQLite
conn = sqlite3.connect('example.db')

# Сохранение датафрейма в таблицу базы данных SQLite
df.to_sql('example', conn, if_exists='replace', index=False)

# Закрытие соединения с базой данных SQLite
conn.close()

# Цифровизация =)
df['fact'] = pd.to_numeric(df['fact'], errors='coerce').dropna()
df['Unnamed: 3'] = pd.to_numeric(df['Unnamed: 3'], errors='coerce').dropna()
df['Unnamed: 4'] = pd.to_numeric(df['Unnamed: 4'], errors='coerce').dropna()
df['Unnamed: 5'] = pd.to_numeric(df['Unnamed: 5'], errors='coerce').dropna()

df['forecast'] = pd.to_numeric(df['forecast'], errors='coerce').dropna()
df['Unnamed: 7'] = pd.to_numeric(df['Unnamed: 7'], errors='coerce').dropna()
df['Unnamed: 8'] = pd.to_numeric(df['Unnamed: 8'], errors='coerce').dropna()
df['Unnamed: 9'] = pd.to_numeric(df['Unnamed: 9'], errors='coerce').dropna()

# Расчет сумм
sum_fact_qliq_data1 = df['fact'].sum()
sum_fact_qliq_data2 = df['Unnamed: 3'].sum()
sum_fact_qoil_data1 = df['Unnamed: 4'].sum()
sum_fact_qoil_data2 = df['Unnamed: 5'].sum()

sum_forecast_qliq_data1 = df['forecast'].sum()
sum_forecast_qliq_data2 = df['Unnamed: 7'].sum()
sum_forecast_qoil_data1 = df['Unnamed: 8'].sum()
sum_forecast_qoil_data2 = df['Unnamed: 9'].sum()

# Вывод Total в консоль
print('Total Fact Qliq data1:',sum_fact_qliq_data1)
print('Total Fact Qliq data2:',sum_fact_qliq_data2)
print('Total Fact Qoil data1:',sum_fact_qoil_data1)
print('Total Fact Qoil data2:',sum_fact_qoil_data2)

print('Total Forecast Qliq data1:',sum_forecast_qliq_data1)
print('Total Forecast Qliq data2:',sum_forecast_qliq_data2)
print('Total Forecast Qoil data1:',sum_forecast_qoil_data1)
print('Total Forecast Qoil data2:',sum_forecast_qoil_data2)