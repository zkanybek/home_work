import sqlite3

# Подключение к базе данных (создаст файл BirdFactory.db)
conn = sqlite3.connect("BirdFactory.db")
cursor = conn.cursor()

# Создание таблицы birdbreeds
cursor.execute("""
CREATE TABLE IF NOT EXISTS birdbreeds (
    breed_id INTEGER PRIMARY KEY AUTOINCREMENT,
    breed_name TEXT UNIQUE NOT NULL,
    description TEXT
)
""")

# Создание таблицы employees
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT NOT NULL,
    position TEXT,
    salary REAL
)
""")

# Добавление данных в таблицу birdbreeds
birdbreeds_data = [
    (1, "Parrot", "The African Grey is believed to have originated in the West and Central African rainforests."),
    (2, "Canary", "The Canary,a small yellow bird belonging to the finch family, is native to western and central parts of Southern Africa."),
    (3, "Cockatiel", "These medium-sized birds are simply a delight to keep."),
    (4, "Dove", "Doves are known for their sweet and gentle dispositions."),
    (5, "Finch", "Finches and canaries (a species of finch) are ever-popular companion birds."),
    (6, "Parrotlet", "What is a Parrotlet? A member of the Psittacidae family, a parrotlet is the smallest species of parrot.")
]

cursor.executemany("""
INSERT OR IGNORE INTO birdbreeds (breed_id, breed_name, description)
VALUES (?, ?, ?)
""", birdbreeds_data)

# Добавление данных в таблицу employees
employees_data = [
    (100, "Marsimov H", "Director", 150000),
    (101, "Matkasymova E", "Menedjer", 20000),
    (102, "Kasymov R", "Rabotnik", 10000),
    (103, "Aidarova A", "Rabotnik", 10000),
    (104, "Farhatov G", "Veterinar", 300000)
]

cursor.executemany("""
INSERT OR IGNORE INTO employees (employee_id, employee_name, position, salary)
VALUES (?, ?, ?, ?)
""", employees_data)

# Сохранение изменений
conn.commit()

# Вывод таблиц
print("Bird Breeds:")
for row in cursor.execute("SELECT * FROM birdbreeds"):
    print(row)

print("\nEmployees:")
for row in cursor.execute("SELECT * FROM employees"):
    print(row)

# Закрытие соединения
conn.close()
