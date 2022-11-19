<h1 align="center">Voice Stickers Telegram bot</h1>
<h2 align="center"><i>Main version</i></h2>

---

**Голосовой Стикер бот Телеграм** - функциональный бот Телеграм, в идею которого легла работа другого голосового бота `@vosticksbot`

**Отличия** данного бота заключаются в:

* Открытый исходный код бота
* Легкий запуск бота с помощью **одной кнопки** благодаря использованию Docker-compose
* Функциональность и реализация **Админ версии** и **Инлайн версии** бота
* Полная свобода в расширении и конструировании собственного бота на основе представленного

---

## Инструментарий проекта:

* `Python 3.10.8`
* `PostgreSQL `
* `FastAPI`
* `HTTPX`
* `Aiogram`
* `Psycopg2`
* `Pydantic`
* `Dotenv`
* `Docker` и `Docker Compose`
---
## Директория проекта:

```
voice_stickers_telegram/
│   README.md
│   docker-compose.yml
|   .gitignore   
│
└───app/
│   |   .env
|   |   create.py
|   |   Dockerfile
|   |   main.py
|   |   requirements.txt
|   |
│   └───errors/
|   |   |   __init__.py
|   |   |   not_modified.py   
|   |   |
│   └───handlers/
|   |   |   __init__.py
|   |   |   add_voices.py
|   |   |   inline_handler.py
|   |   |   manage_voices.py
|   |   |   sort_by_tags.py
|   |   |   start_chat.py
|   |   |
|   └───keyboard/
|   |   |   __init__.py
|   |   |   kb_cancel.py
|   |   |   kb_start.py
|   |   |   
└───api/
|   │   Dockerfile
|   |   requirements.txt
|   |   server.py
|   |   
|   └───database/
|   |   |   __init__.py
|   |   |   postgres.py
|   |   |
└───postgres_database/
|   |   create_fixtures.sql
|   |   Dockerfile
```

## Требования:

Python 3.10.8+
Docker
_Возможно тестирование работы на более ранних версий Python_
_Проверяйте совместимость по работе установленных библиотек_

---

## Установка:

### Первичная инициализация проекта:

```console
$ git clone https://github.com/JackOman69/voice_stickers_telegram.git
```
<a href="https://docs.docker.com/desktop/">Docker Desktop</a>

### Настройка бота:

* Заходим в Телеграм и создаем своего бота в `@botfather`
* Копируем API ключ и включаем боту режим `Inline` через `Settings`

### Изменение create-fixtures.sql:

* `create-fixtures.sql` - файл инициализации базы данных, по желанию можете изменить название вашей БД

### Установка .env:

* Создайте файл `.env` в директории `/app` и вложите туда 2 переменные:

```python
TOKEN="ключ_вашего_бота"
ADMIN_ID="ID Администраторов, у которых будет доступ к Админ панели (Через запятую)"
```

* Создайте файл `.env` в директории `/api` и вложите туда 4 переменные:

```python
HOST="Название вашего контейнера с postgresql из docker-compose.yml"
USER="Логин для аутентификации к БД"
PASSWORD="Пароль для аутентификации к БД"
DB_NAME="Название вашей БД из /postgres_database/create_fixtures.sql"
```

---

## Запуск

### Запуск docker-а:

* Запускать проект нужно с помощью следующих команд:

```console
$ docker-compose build

$ docker-compose up
``` 

---

## Проверка:

* Проверка работоспособности контейнеров осуществляется в `Docker Desktop`
* Для проверки `API` переходим на `127.0.0.1:80/docs` и проверяем страницу сваггера со всеми имеющимися методами (Всего их 10)

---

## Релиз версий:

* `19.11.2022`
* Исправление мелких багов
* Доработка сортировки по авторам, тегам
* Добавление возможности редактирования голосового внутри Админ панели

* `16.11.2022`
* Релиз проекта на гитхаб