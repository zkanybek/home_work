# Импортируем библиотеку pandas
# Она используется для работы с табличными данными (анализ, фильтрация, статистика)
import pandas as pd

# Создаем словарь с данными: список имён, возрастов и городов
data = {
    "Имя": ["Алиса", "Боб", "Клара"],
    "Возраст": [25, 30, 22],
    "Город": ["Москва", "Казань", "Новосибирск"]
}

# Преобразуем словарь в DataFrame — это основная структура данных в pandas, похожая на таблицу
df = pd.DataFrame(data)

# Выводим всю таблицу (DataFrame)
print("Исходный DataFrame:\n", df)

# Строим базовую статистику по колонке "Возраст" (среднее, минимум, максимум и др.)
print("\nСтатистика по возрасту:\n", df["Возраст"].describe())

# Фильтруем таблицу: оставляем только строки, где возраст больше 23 лет
older_than_23 = df[df["Возраст"] > 23]

# Показываем отфильтрованные данные
print("\nЛюди старше 23 лет:\n", older_than_23)
