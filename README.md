<h1 align="center">Voice Stickers Telegram bot</h1>
<h2 align="center"><i>Light version</i></h3>

## Описание

Представляю вашему вниманию: Телеграм бот с отправлением голосовых сообщений в инлайн режиме

## Реализация и компоненты:

- Админ-бот с управлением голосовых сообщений и добавлением их в базу данных
- Клиент-бот в инлайн режиме, способствующий использованию голосовых сообщений из базы данных в любом чате

- <i>В Будущем:</i> Аналитика использования бота с технологией Data Science

## Инструменты разработки:

- Python 3.10
- Aiogram 3.0.0b6
- Aiohttp 3.8.1
- Python-dotenv 0.21.0
- SQLite 3

- <i>В основной версии:</i> PostgreSQL, Docker, Docker-Compose

## Инструкция к установке:

- git clone https://github.com/JackOman69/voice_stickers_telegram -b light-version
- python -m venv venv
- & <i>Путь до проекта</i>/voice_stickers_telegram/venv/Scripts/Activate.ps1
- pip install -r requirements.txt
- Создайте в корневой папке файл .env, куда добавьте строку <i>TOKEN=*ВАШ ТОКЕН БОТА*</i>
- Измените в файле handlers/start_chat.py константу ADMIN_ID на ваш ID или ID всех людей, кто будет пользоваться админкой
- python main.py


<h1 align="center">Обновления в пути!</h1>