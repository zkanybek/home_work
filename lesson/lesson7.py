import sqlite3


# A4
connect = sqlite3.connect('Users.db')
# Рука с Ручкой
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (50) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()


# CRUD - Create - Read - Update - Delete

# DROP DATA BASE
def add_user(name_1, age_1, hobby_1):
    cursor.execute(
        f'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name_1, age_1, hobby_1)
    )
    connect.commit()
    print(f"Пользователь добавлен: {name_1}")

# name = input("Введите ваше имя")

add_user("Test", 33, "Плавать")


def get_all_user():
    cursor.execute('SELECT * FROM users')

    users = cursor.fetchall()

    print(users)

    if users:
        print("Список всех пользователей!!")

        for i in users:
            print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
    else:
        print("Список пуст!!")

# get_all_user()


def update_user_by_id(name, id):
    cursor.execute(
        'UPDATE users SET name = ? WHERE rowid = ?',
        (name, id)
    )
    connect.commit()
    print('пользователь обновлен!!')


# update_user_by_id("Arzybek", 3)


def delete_user_by_id(id):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (id,)
    )
    connect.commit()
    print("Пользователь удален!!")

# delete_user_by_id(2)
