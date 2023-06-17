import requests
import logging

from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token='')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'buttons'])
async def new_button(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons1 = ["cat", "dog"]
    buttons2 = ["duck", "fox"]
    keyboard.add(*buttons1)
    keyboard.add(*buttons2)
    await message.answer("Use buttons to get animal images!", reply_markup=keyboard)


@dp.message_handler(content_types='text')
async def show_animal(message: types.Message):
    new_message = message.text.lower().strip()
    dict_animals = {'cat':'https://aws.random.cat/meow', 'dog':'https://random.dog/woof.json',
                    'duck':'https://random-d.uk/api/v2/random', 'fox':'https://randomfox.ca/floof/'}
    if new_message in dict_animals:
        res = requests.get(dict_animals[new_message])
        if res:
            file = res.json()['file']
            json_file = res.json()
            file = ''
            if 'file' in json_file:
                file = res.json()['file']
            elif 'url' in json_file:
                file = res.json()['url']
            elif 'image' in json_file:
                file = res.json()['image']

            if file:
                await message.answer(file)
    else:
        await message.answer('I don\'t know such type of animal.\nCurrently supported these types of animals: ' + ', '.join(dict_animals.keys()))


# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
