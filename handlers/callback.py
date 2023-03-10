from aiogram import types, Dispatcher
from config import bot


# @dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Answer:"
    answers = [
        '[4]',
        '[8]',
        '[4, 6]',
        '[2, 4]',
        '[5]',
    ]

    photo = open("media/problem1.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation="IZI",
        open_period=60,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
