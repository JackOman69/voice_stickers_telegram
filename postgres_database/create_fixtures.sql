CREATE TABLE IF NOT EXISTS voicestickers(
    id INTEGER GENERATED ALWAYS AS IDENTITY, 
    voice TEXT, 
    name TEXT, 
    description TEXT, 
    tags TEXT, 
    author TEXT, 
    created_date TEXT, 
    admin_author_id INTEGER
)