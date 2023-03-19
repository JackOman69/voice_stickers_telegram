import logging
import asyncio
from create import dp, bot
from handlers import add_voices, start_chat, sort_by_tags, inline_handler, manage_voices, edit_voices
from errors import not_modified


async def main():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    dp.include_router(not_modified.router)
    dp.include_router(inline_handler.router)
    dp.include_router(start_chat.router)
    dp.include_router(sort_by_tags.router)
    dp.include_router(manage_voices.router)
    dp.include_router(edit_voices.router)
    dp.include_router(add_voices.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
