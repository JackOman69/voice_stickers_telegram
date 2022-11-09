<h1 align="center">Voice Stickers Telegram bot</h1>
<h2 align="center"><i>Light version</i></h3>

## Описание

Представляю вашему вниманию: Телеграм бот с отправлением голосовых сообщений в инлайн режиме

## Реализация и компоненты:

- Админ-бот с управлением голосовых сообщений и добавлением их в базу данных
- Инлайн режим бота, способствующий использованию голосовых сообщений из базы данных в любом чате
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
- `venv/Scripts/Activate` Для активации виртуального окружения
- `pip install -r requirements.txt`
- Создайте в корневой папке файл .env и добавьте две строки: 
- `TOKEN="ВАШ_ТОКЕН_БОТА"`- Токен вашего бота 
- `ADMIN_ID="ID Администраторов"`- ID пользователей, у которых будет доступ к Админке бота
- `python main.py`

## Обновления:

- `30.10.2022` | Релиз бота на Aiogram 2.22
- `01.11.2022` | Переход бота на версию Aiogram 3.0.0b3
- `09.11.2022` | Полноценный релиз бота с использованием SQLite3

<h1 align="center">Обновления в пути!</h1>
