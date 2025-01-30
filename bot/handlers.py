import httpx
from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

from bot.state import AddIMEIState
from bot.validators import validate_imei
from config import settings, WHITELIST

dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def start(message: Message, state: FSMContext) -> None:
    if message.from_user.id not in WHITELIST:
        await message.answer(
            text="Вы не зарегистрированы. Доступ запрещен",
        )
        return
    await message.answer(text="Привет! Отправь мне IMEI для проверки.")
    await state.set_state(AddIMEIState.waiting_for_imei)


@dp.message(AddIMEIState.waiting_for_imei)
async def proccess_imei(message: Message, state: FSMContext) -> None:
    imei: str = message.text.strip()
    is_valid: bool = validate_imei(imei)
    if not is_valid:
        await message.edit_text(text="Неверный IMEI")
        return

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"http://{settings.API_HOST}:{settings.API_PORT}/check-imei",
                json={
                    "deviceId": imei,
                    "serviceId": 12
                },
                headers={"token": settings.IMEICHECK_API_SANDBOX_TOKEN},
            )
            response.raise_for_status()
            result = response.json()

        response_message = (
            f"IMEI: {result["properties"]["imei"]}\n"
            f"Название: {result["properties"]["deviceName"]}\n"
            f"Статус: {result.get("status")}\n"
            f"Описание: {result["properties"]["modelDesc"]}"
        )
        await message.answer(response_message)

    except httpx.HTTPStatusError as e:
        await message.answer(f"Ошибка API: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}")
    finally:
        await state.clear()
