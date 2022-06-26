from aiogram import Bot, Dispatcher, types, executor

TOKEN = '1387776977:AAH0xe4Rw_8nzH_0NkppYpnFKwZTQk5D_o0'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def send_welcome(message: types.Message):
    await message.reply_to_message(f'Я Аббат Вестминстера. Приятно познакомиться, {msg.from_user.first_name}')

async def get_text_messages(message: types.Message):
   if message.text.lower() == 'привет':
       await message.answer('Привет!')
   elif message.text.lower() == 'Как дела?':
       await message.answer('Всё пучком!')
   else:
       await message.answer('Не понимаю, что это значит.')

dp.register_message_handler(send_welcome, commands=['start', 'help'])
dp.register_message_handler(get_text_messages, content_types=['text'])

if __name__ == '__main__':
   executor.start_polling(dp)
