from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'TOKEN ТВОЕГО БОТА'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Ты меня включил командой /start")
    
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    
    # тут бот отвечает на сообщения
    if message.text.lower() == 'привет':
      await message.answer("Привет, друг еще раз!")
    elif message.text.lower() == 'как дела?':
      await message.answer("Отлично! Ты как?")
      
# ЗАПУСК ДОМА
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
