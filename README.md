<h1 align="center">Voice Stickers Telegram bot</h1>
<h2 align="center"><i>Light version</i></h3>

## Описание

Представляю вашему вниманию: Телеграм бот с отправлением голосовых сообщений в инлайн режиме

## Реализация и компоненты:

- Админ-бот с управлением голосовых сообщений и добавлением их в базу данных
- Клиент-бот в инлайн режиме, способствующий использованию голосовых сообщений из базы данных в любом чате
- <i>В Будущем: Аналитика использования бота с технологией Data Science</i>

## Инструменты разработки:

- Python 3.10
- Aiogram 3.0.0b6
- Aiohttp 3.8.1
- Python-dotenv 0.21.0
- SQLite 3
- <i>В основной версии: PostgreSQL, Docker, Docker-Compose</i>

## Инструкция к установке:

- `git clone https://github.com/JackOman69/voice_stickers_telegram -b light-version`
- `python -m venv venv`
- `& /Путь до проекта/voice_stickers_telegram/venv/Scripts/Activate.ps1`
- `pip install -r requirements.txt`
- Создайте в корневой папке файл .env, куда добавьте строку `TOKEN="ВАШ_ТОКЕН_БОТА"`
- Измените в файле `handlers/start_chat.py` константу `ADMIN_ID` на ваш ID или ID всех людей, кто будет пользоваться админкой
- `python main.py`


<h1 align="center">Обновления в пути!</h1>
