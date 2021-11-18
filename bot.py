import config
import requests
import logging

from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO, filename="sample.log")

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


# echo
@dp.message_handler(lambda message: message.text == "Новый котик")
async def echo(message: types.Message):
    res = requests.get('https://aws.random.cat/meow')
    if res:
        res_json = res.json()
        file = res_json['file']
        await message.answer(file)


@dp.message_handler(commands=['start', 'cat_button'])
# @dp.message_handler(commands="start")
async def new_button(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text="Новый котик")
    keyboard.add(button)
    await message.answer("Используйте кнопку для получения котика!", reply_markup=keyboard)
    # res = requests.get('https://aws.random.cat/meow')
    # if res:
    #     res_json = res.json()
    #     file = res_json['file']
    #     await message.answer(file)


# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
