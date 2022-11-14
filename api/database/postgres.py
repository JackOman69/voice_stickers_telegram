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

# GET Queries
def voice_by_id(data):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM voicestickers_db WHERE id = %s", (data, ))
        by_id = cursor.fetchall()
        return by_id

def voice_by_name(data):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM voicestickers_db WHERE name = %s", (data, ))
        by_name = cursor.fetchall()
        return by_name

def voice_by_tag(data):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM voicestickers_db WHERE tags = %s", (data, ))
        by_tag = cursor.fetchall()
        return by_tag

def voice_by_author(data):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM voicestickers_db WHERE author = %s", (data, ))
        by_author = cursor.fetchall()
        return by_author

# POST Queries
# def create_the_voice():
#     with connection.cursor() as cursor: