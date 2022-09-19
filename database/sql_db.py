import sqlite3
from create import bot

def sql_start():
    global db, cursor
    db = sqlite3.connect("database/shiz.db")
    cursor = db.cursor()
    initialization_query = """CREATE TABLE IF NOT EXISTS shizics(photo TEXT, name TEXT PRIMARY KEY, description TEXT, rarity TEXT)"""
    cursor.execute(initialization_query)
    db.commit()

async def sql_add(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO shizics VALUES (?, ?, ?, ?)", tuple(data.values()))
        db.commit()
        
async def sql_read(message):
    for i in cursor.execute("SELECT * FROM shizics").fetchall():
        await bot.send_photo(message.from_user.id, i[0], f"{i[1]}\nОписание шизоида: {i[2]}\nРедкость шизоида: {i[3]}")
