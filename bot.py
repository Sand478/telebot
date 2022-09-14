import logging
import os
from posixpath import split

from aiogram import Bot, Dispatcher, executor, types

#TOKEN = os.getenv('TOKEN') #получаем токен из переменной DOCKER
from config import TOKEN  #получаем токен из соседнего файла в папке при запуске в IDE

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message:types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Hellow, {user_name}!"
    logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
    await message.reply(text)

@dp.message_handler()
async def send_welcome(message:types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    rus_list = list(text.upper())
    en_list = []
    for i in rus_list:
        if i == 'А':
            en_list.append('A')
        elif i == 'Б':
            en_list.append('B')
        elif i == 'В':
            en_list.append('V')
        elif i == 'Г':
            en_list.append('G')
        elif i == 'Д':
            en_list.append('D')
        elif i == 'Е':
            en_list.append('E')
        elif i == 'Ё':
            en_list.append('E')
        elif i == 'Ж':
            en_list.append('ZH')
        elif i == 'З':
            en_list.append('Z')
        elif i == 'И':
            en_list.append('I')
        elif i == 'Й':
            en_list.append('I')
        elif i == 'К':
            en_list.append('K')
        elif i == 'Л':
            en_list.append('L')
        elif i == 'М':
            en_list.append('M')
        elif i == 'Н':
            en_list.append('N')
        elif i == 'О':
            en_list.append('O')
        elif i == 'П':
            en_list.append('P')
        elif i == 'Р':
            en_list.append('R')
        elif i == 'С':
            en_list.append('S')
        elif i == 'Т':
            en_list.append('T')
        elif i == 'У':
            en_list.append('U')
        elif i == 'Ф':
            en_list.append('F')
        elif i == 'Х':
            en_list.append('KH')
        elif i == 'Ц':
            en_list.append('TS')
        elif i == 'Ч':
            en_list.append('CH')
        elif i == 'Ш':
            en_list.append('SH')
        elif i == 'Щ':
            en_list.append('SHCH')
        elif i == 'Ь':
            en_list.append('')
        elif i == 'Ы':
            en_list.append('Y')
        elif i == 'Ъ':
            en_list.append('IE')
        elif i == 'Э':
            en_list.append('E')
        elif i == 'Ю':
            en_list.append('IU')
        elif i == 'Я':
            en_list.append('IA')
        else:
            en_list.append(i)
        text = ''.join(en_list)
    logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
    await bot.send_message(user_id, text)


if __name__ == '__main__':
    executor.start_polling(dp)