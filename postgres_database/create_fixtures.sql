CREATE TABLE IF NOT EXISTS voicestickers(
    id INTEGER GENERATED ALWAYS AS IDENTITY, 
    voice VARCHAR(255), 
    name VARCHAR(255), 
    description VARCHAR(255), 
    tags VARCHAR(255), 
    author VARCHAR(255), 
    created_date VARCHAR(255), 
    admin_author_id INTEGER
);
INSERT INTO voicestickers(
    voice, name, description, tags, author, created_date, admin_author_id
) VALUES(
        'AwACAgIAAxkBAAIHEmNW23daXDhXLqCvjdd0UhrF7lMMAALKHgAC8f2wSp7iJad51mC3KgQ', 
        'Наелся', 
        'Наелся, Леха', 
        'наелся, леха', 
        'Леха', 
        '2022-10-24 21:37:59', 
        '509237723'
    );
INSERT INTO voicestickers(
    voice, name, description, tags, author, created_date, admin_author_id
) VALUES(
        'AwACAgIAAxkBAAIHZGNW3dl4x4gO6Q5lj-OIvSoyyb1LAAJaHwACD1e4SjtAw-aQiK4vKgQ', 
        'Превращение в карбодеда', 
        'Особый обряд по превращению молодого деда в карбо деда, троение пердение и чихание признак познания вековых секретов', 
        'карбодед', 
        'Съебоба', 
        '2022-10-24 21:49:38', 
        '440280067'
    );
INSERT INTO voicestickers(
    voice, name, description, tags, author, created_date, admin_author_id
) VALUES(
        'AwACAgIAAxkBAAIKLWNaoy1OJU-249pE8K0Jer4UcSz7AAJxIAACuhfQSn1vT36QJ9X2KgQ', 
        'Название', 
        'Описание', 
        'леха, наелся', 
        'Леха', 
        '2022-10-27 18:26:52', 
        '509237723'
    );
