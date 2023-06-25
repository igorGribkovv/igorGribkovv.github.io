from aiogram import Bot, Dispatcher, executor,  types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6220229259:AAGPc32S3KAygy2TEl1McRH8P-E-YnXQh5I')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.KeyboardButton('OPEN', web_app=WebAppInfo(url='aio.html')))
    await message.answer('Hallo friend', reply_markup=markup)

executor.start_polling(dp)