import telebot


TOKEN = '5192002387:AAGpDexssm-XRbFGUW3SYv3HOhomUVnx494'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Hello")






    bot.polling() 