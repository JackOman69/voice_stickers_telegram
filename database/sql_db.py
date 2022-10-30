import sqlite3

def sql_start():
    global db, cursor
    db = sqlite3.connect("database/voices.db")
    cursor = db.cursor()
    initialization_query = """CREATE TABLE IF NOT EXISTS voicestickers(id INTEGER PRIMARY KEY, voice TEXT, name TEXT, description TEXT, tags TEXT, author TEXT, created_date TEXT, admin_author_id INT)"""
    cursor.execute(initialization_query)
    db.commit()

async def sql_add(state):
    async with state.proxy() as data:
        cursor.execute("""SELECT datetime("now","localtime")""")
        cursor.execute("""INSERT INTO voicestickers(voice, name, description, tags, author, created_date, admin_author_id) VALUES (?, ?, ?, ?, ?, datetime("now","localtime"), ?)""", tuple(data.values()))
        db.commit()

async def sql_read_author():
    return cursor.execute("SELECT author FROM voicestickers").fetchall()

async def sql_sort_by_tags(data):
    return cursor.execute("SELECT * FROM voicestickers WHERE instr(tags, ?) > 0", (data, )).fetchall()

async def sql_sort_by_authors(data):
    return cursor.execute("SELECT tags FROM voicestickers WHERE instr(author, ?) > 0", (data, )).fetchall()

async def sql_edit(data):
    return cursor.execute("SELECT * FROM voicestickers WHERE id == ?", (data, )).fetchall()

async def sql_delete(data):
    cursor.execute("DELETE FROM voicestickers WHERE id == ?", (data, )).fetchall()
    db.commit()
