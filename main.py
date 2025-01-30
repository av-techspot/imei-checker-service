import logging

import asyncio
import uvicorn
from aiogram import Bot
from fastapi import FastAPI

from api.endpoints import api_router
from bot.handlers import dp as bot_dispatcher
from config import settings


async def main():
    app = FastAPI(name="imei-checker-api", title="IMEI Checker API")
    app.include_router(api_router)

    bot = Bot(token=settings.BOT_TOKEN)
    dp = bot_dispatcher

    asyncio.create_task(dp.start_polling(bot))

    config = uvicorn.Config(
        app=app,
        host=settings.API_HOST,
        port=settings.API_PORT,
    )
    server = uvicorn.Server(config)

    try:
        await server.serve()
    finally:
        if server.started:
            await bot.session.close()
            await server.shutdown()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(main())
