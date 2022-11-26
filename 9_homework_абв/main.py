from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5712662084:AAEHqQVWAJNeLaa7j8tZdOcxj59Dg5ZzYq4')
updater = Updater(token='5712662084:AAEHqQVWAJNeLaa7j8tZdOcxj59Dg5ZzYq4')
dispatсher =  updater.dispatcher

def start(update,context):                     
    text = update.message.text.split()
    list = []
    for letter in text:
        if "абв" not in letter :
           list.append(letter)         
    context.bot.send_message(update.effective_chat.id, ' '.join(list))

start_handler = MessageHandler(Filters.text, start)
dispatсher.add_handler(start_handler)          

updater.start_polling()                        # начало бота
updater.idle()                                 # конец бота  



