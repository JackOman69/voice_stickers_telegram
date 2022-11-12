import psycopg2
from dotenv import load_dotenv, find_dotenv 
import os

load_dotenv(find_dotenv())

def initialization_db():
    connection = None
    try:
        connection = psycopg2.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("""SELECT version();""")
            print(f"[INFO] Version: {cursor.fetchone()}" )

        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS voicestickers(
                            id SERIAL PRIMARY KEY, 
                            voice TEXT, 
                            name TEXT, 
                            description TEXT, 
                            tags TEXT, 
                            author TEXT, 
                            created_date TEXT, 
                            admin_author_id INTEGER)""")
    
            print("[INFO] Successfully!")

    except Exception as ex:
        print("[INFO] Some exceptions were raised: ", ex)
    # finally:
    #     connection.close()
    #     print("[INFO] Database is closed")

initialization_db()