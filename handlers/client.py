from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from keyboards.client_kb import start_markup


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_message(message.from_user.id,
                           f"Салалекум хозяин {message.from_user.first_name}",
                           reply_markup=start_markup)
    # await message.answer("This is an answer method!")
    # await message.reply("This is a reply method")


async def info_handler(message: types.Message):
    await message.answer("Сам разбирайся!!")


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "By whom invented Python?"
    answers = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]

    await bot.send_poll(
        message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation="IZI",
        open_period=60,
        reply_markup=markup
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(info_handler, commands=['info'])