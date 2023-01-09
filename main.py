from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
import logging

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Салалекум хозяин {message.from_user.first_name}")
    await message.answer("This is an answer method!")
    await message.reply("This is a reply method")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
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
    )


@dp.message_handler()
async def echo(message: types.Message):
    # print(message)
    await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
