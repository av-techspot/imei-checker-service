from aiogram.fsm.state import State, StatesGroup


class AddIMEIState(StatesGroup):
    waiting_for_imei = State()
