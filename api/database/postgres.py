import psycopg2
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

try:
    connection = psycopg2.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    print("[INFO] Connection was successful!")
    connection.autocommit = True
except Exception as ex:
    print("[INFO] EXCEPTIONS: ", ex)


def id_created_voice():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM voicestickers ORDER BY id DESC LIMIT 1")
        return cursor.fetchone()[0]


def check_deleted_voice(data):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM voicestickers WHERE id = %s", (data, ))
        try:
            cursor.fetchone()[0]
        except:
            return True


# ----------------- GETTERS -----------------
def get_all():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM voicestickers")
        by_all = cursor.fetchall()
        return by_all


def voice_by_id(id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM voicestickers WHERE id = %s", (id, ))
        by_id = cursor.fetchall()
        return by_id


def voice_by_name(name):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM voicestickers WHERE POSITION(%s in name) > 0", (name, ))
        by_name = cursor.fetchall()
        return by_name


def voice_by_tag(tags):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM voicestickers WHERE %s = ANY (tags)", (tags, ))
        by_tag = cursor.fetchall()
        return by_tag


def tags_sorted_by_authors(author):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT tags FROM voicestickers WHERE author = %s", (author, ))
        by_author = cursor.fetchall()
        return by_author


def voice_by_author(author):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM voicestickers WHERE author = %s", (author, ))
        by_author = cursor.fetchall()
        return by_author


def all_voices_by_author():
    with connection.cursor() as cursor:
        cursor.execute("SELECT author FROM voicestickers")
        by_author = cursor.fetchall()
        return by_author
# ----------------- GETTERS -----------------


# ----------------- MIGRATIONS -----------------
def create_the_voice(voice, name, description, tags, author, admin_author_id):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO voicestickers(voice, name, description, tags, author, created_date, admin_author_id) VALUES (%s, %s, %s, %s, %s, LOCALTIMESTAMP(0), %s)",
                       (voice, name, description, tags, author.capitalize(), admin_author_id, ))


def delete_the_voice(id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM voicestickers WHERE id = %s", (id, ))


def edit_the_voice(name, description, tags, author, id):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE voicestickers SET name = %s, description = %s, tags = %s, author = %s WHERE id = %s",
                       (name, description, tags, author, id, ))
# ----------------- MIGRATIONS -----------------
