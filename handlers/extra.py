from aiogram import types, Dispatcher
from config import bot
from test import get_message


async def echo(message: types.Message):
    await message.answer(get_message(message))
    # bad_words = ['java', 'html', 'дурак', "дура"]
    # username = f"@{message.from_user.username}" \
    #     if message.from_user.username is not None else message.from_user.first_name
    # for word in bad_words:
    #     if word in message.text.lower().replace(' ', ''):
    #         # DRY - Don't Repeat Yourself
    #         await message.answer(f"Не матерись {username}"
    #                              f" сам ты {word}!")
    #
    # if message.text.startswith('.'):
    #     await bot.pin_chat_message(message.chat.id, message.message_id)
    #
    # if message.text == 'dice':
    #     a = await bot.send_dice(message.chat.id, emoji='🎯')
    #     # print(a.dice.value)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
