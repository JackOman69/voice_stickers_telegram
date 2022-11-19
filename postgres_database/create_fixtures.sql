CREATE TABLE IF NOT EXISTS voicestickers(
    id INTEGER GENERATED ALWAYS AS IDENTITY, 
    voice VARCHAR(255), 
    name VARCHAR(50), 
    description TEXT, 
    tags TEXT [], 
    author VARCHAR(50), 
    created_date VARCHAR(50), 
    admin_author_id INTEGER
);