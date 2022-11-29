from controller import parse_data, data_calculation
from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from log import get_id_user, get_input_data, get_result, save_log

bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher

start_calc = 0

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет! Я простой бот-калькулятор!')
    context.bot.send_message(update.effective_chat.id, 'Если захочешь закончить работу, нажми /end')
    get_id_user(update.effective_chat.id)
    return start_calc

def get_data(update, context):
    data = update.message.text
    get_input_data(data)                                            # передаем данные для записи в log
    list_data = parse_data(data)                                    
    result = data_calculation(list_data)                            # получаем результат
    get_result(result)                                              
    save_log()                                                      # записываем полученный результат в log
    context.bot.send_message(update.effective_chat.id, f'Полученнный результат: {result}')

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Пока!')
    return ConversationHandler.END

start_handler = CommandHandler('start', start)
get_data_handler = MessageHandler(Filters.text & (~Filters.command), get_data)
mes_data_handler = CommandHandler('end', cancel)

conv_handler = ConversationHandler(entry_points = [start_handler],
                                   states = {start_calc: [get_data_handler]},
                                   fallbacks = [mes_data_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()