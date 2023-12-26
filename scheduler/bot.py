import os
import telebot

TOKEN = os.environ.get('TG_TOKEN')
bot = telebot.TeleBot(TOKEN)
bot.remove_webhook()


@bot.message_handler(commands=['start'])
def start_message(message):
    """ Функция вывода при старте: приветствие """
    msg = 'Ну что готов к поиску работы?'
    bot.send_message(message.chat.id, msg)


def start():
    """ Запуск бота """
    while True:
        bot.polling(none_stop=True, skip_pending=True)
