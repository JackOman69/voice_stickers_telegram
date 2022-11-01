import logging
import asyncio
from create import dp, bot
from handlers import add_voices, start_chat, sort_by_tags
from database.sql_db import sql_start

async def main():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    sql_start()

    dp.include_router(start_chat.router)
    dp.include_router(sort_by_tags.router)
    dp.include_router(add_voices.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())