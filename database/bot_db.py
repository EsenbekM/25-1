# SQL - Structured Query Language
# СУБД - Система Управления Базой Данных
# CRUD = Create Read Update Delete
import random
import sqlite3

from config import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS anketa "  # rows
               "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
               "t_id INTEGER UNIQUE, "
               "username VARCHAR (255), "
               "name VARCHAR (255), "
               "age INTEGER, "
               "gender VARCHAR (255), "
               "region TEXT, "
               "photo TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anketa "
                       "(t_id, username, name, age, gender, region, photo) VALUES "
                       "(?, ?, ?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM anketa").fetchall()
    random_user = random.choice(result)
    await bot.send_photo(
        message.from_user.id,
        random_user[-1],
        caption=f"{random_user[3]} {random_user[4]} {random_user[5]} "
                f"{random_user[6]}\n\n{random_user[2]}"
    )


async def sql_command_all():
    return cursor.execute("SELECT * FROM anketa").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (user_id,))
    db.commit()
