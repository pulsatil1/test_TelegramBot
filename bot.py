import config
import requests
import logging

from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'buttons'])
# @dp.message_handler(commands="start")
async def new_button(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # button = types.KeyboardButton(text="Котик")
    buttons1 = ["Котик", "Пёсик"];
    buttons2 = ["Уточка", "Лисичка"];
    keyboard.add(*buttons1)
    keyboard.add(*buttons2)
    await message.answer("Используйте кнопки для получения животных!", reply_markup=keyboard)


@dp.message_handler(content_types='text')
async def show_cat(message: types.Message):
    new_message = message.text.lower().strip()
    if new_message in ['котик', 'кот', 'кошка', 'кошак', 'котяра', 'котейка', 'кошечка', 'cat']:
        res = requests.get('https://aws.random.cat/meow')
        if res:
            file = res.json()['file']
            await message.answer(file)
    elif new_message in ['пес', 'пёс', 'песик', 'пёсик', 'песель', 'пёсель', 'собака', 'собачка', 'dog', 'doggy']:
        res = requests.get('https://random.dog/woof.json')
        if res:
            file = res.json()['url']
            await message.answer(file)
    elif new_message in ['утка', 'уточка', 'утя', 'утенок', 'утёнок', 'ducky']:
        res = requests.get('https://random-d.uk/api/v2/random')
        if res:
            file = res.json()['url']
            await message.answer(file)
    elif new_message in ['лиса', 'лисичка', 'лисица', 'лис', 'fox', 'foxy']:
        res = requests.get('https://randomfox.ca/floof/')
        if res:
            file = res.json()['image']
            await message.answer(file)
    else:
        await message.answer('Я не знаю такого животного')


# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
