import sqlite3

# Подключение к базе данных
connect = sqlite3.connect('Client.db')
cursor = connect.cursor()

# Создание таблицы clients
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        birthday TEXT NOT NULL
    )
''')
connect.commit()

# CREATE
def add_client(name, age, birthday):
    cursor.execute(
        'INSERT INTO clients (name, age, birthday) VALUES (?, ?, ?)',
        (name, age, birthday)
    )
    connect.commit()
    print(f"Клиент добавлен: {name}")

# READ
def get_all_clients():
    cursor.execute('SELECT rowid, * FROM clients')
    clients = cursor.fetchall()

    if clients:
        print("Список всех клиентов:")
        for client in clients:
            print(f"ID: {client[0]}, NAME: {client[1]}, AGE: {client[2]}, BIRTHDAY: {client[3]}")
    else:
        print("Список клиентов пуст.")

# UPDATE
def update_client_name_by_id(new_name, id):
    cursor.execute(
        'UPDATE clients SET name = ? WHERE rowid = ?',
        (new_name, id)
    )
    connect.commit()
    print("Имя клиента обновлено!")

# DELETE
def delete_client_by_id(id):
    cursor.execute(
        'DELETE FROM clients WHERE rowid = ?',
        (id,)
    )
    connect.commit()
    print("Клиент удалён!")

# Примеры вызова функций:
# add_client("Jnybek", 19, "2006-06-25")
# get_all_clients()
# update_client_name_by_id("Zkanybek", 1)
# delete_client_by_id(1)
