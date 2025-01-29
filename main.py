import logging

import asyncio
import uvicorn
from fastapi import FastAPI

from api.api import api_router
from config import settings


async def main():
    app = FastAPI(name="imei-checker-api", title="IMEI Checker API")
    app.include_router(api_router)

    config = uvicorn.Config(
        app=app,
        host=settings.api_host,
        port=settings.api_port,
    )
    server = uvicorn.Server(config)

    try:
        await server.serve()
    finally:
        if server.started:
            await server.shutdown()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(main())
