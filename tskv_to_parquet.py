# %%
import pandas as pd

data = []

# Открываем файл и читаем его построчно
with open('geo-reviews-dataset-2023.tskv', 'r', encoding='utf-8') as file:
    for line in file:
        # Убираем пробельные символы в начале и конце строки
        line = line.strip()
        
        # Создаем словарь для хранения данных из одной строки
        record = {}
        
        # Разделяем строку по символу табуляции '\t'
        fields = line.split('\t')
        
        # Разбираем каждую пару ключ=значение
        for field in fields:
            if '=' in field:
                key, value = field.split('=', 1)  # Разделяем только по первому '='
                if key == 'rating':
                    record[key] = int(value[0])
                else:
                    record[key] = value
        
        # Добавляем словарь в список
        data.append(record)

# Создаем DataFrame из списка словарей
df = pd.DataFrame(data)
# %%
print(df.head(250000))
# %%
df.to_parquet('geo-reviews-dataset-2023.parquet')