# 1. Разворачиваем рубрики в отдельные строки
df_exploded = df.explode('rubrics')

# 2. Сбрасываем индекс, чтобы избежать дублей индексов
df_exploded = df_exploded.reset_index(drop=True)

# 3. Группируем по рубрикам и вычисляем среднюю оценку
rubric_ratings = df_exploded.groupby('rubrics')['rating'].mean()

# 4. Выводим результат
print(rubric_ratings)