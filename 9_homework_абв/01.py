from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint

bot = Bot(token='5712662084:AAEHqQVWAJNeLaa7j8tZdOcxj59Dg5ZzYq4')
updater = Updater(token='5712662084:AAEHqQVWAJNeLaa7j8tZdOcxj59Dg5ZzYq4')
dispatсher =  updater.dispatcher

A = 0
B = 1
С = 2

def start(update,context):                                                                  # в контексте хранятся все встроенные команды
    context.bot.send_message(update.effective_chat.id, 'Привет, \n сколько конфет ты берешь?')
    return A

def win(update, context):                                                                    # Основная функция
    text = int(update.message.text)
    a = select_bot()
    b = select_man(a)
    sum = select_man(a,text)
    context.bot.send_message(update.effective_chat.id, b)
    context.bot.send_message(update.effective_chat.id, f'Ваш выигрыш составляет {sum}')    

def select_bot(update,context,candy, bot_move):                                                      # выбор бота
    text = update.message.text
    max_candy = int(28)
    if candy < max_candy:
        bot_move = candy
        move2 = randint(1, bot_move)
        #print(move2)
        candy = candy - move2
        #print('Осталось -', candy)
        context.bot.send_message(update.effective_chat.id, f'Я взял {candy} конфет')
    context.bot.send_message(update.effective_chat.id, "Теперь бери ты!")   
    #return B

def select_man(update, context, candy, move):                                                        # выбор человека
    text = update.message.text
    candy=int(2021)
    max_candy = int(28)

    for i in range(candy,0,-1):                                                                  
        if i % 2 == 1:
            move = int(input())
            if candy > max_candy:
                if move <= max_candy:
                    candy = candy - move
                else:
                    print('Недопустимое количество взятых конфет, максимально можно взять 28, попробуйте еще раз! ')
                    move = int(input())
                    if move <= max_candy:
                        candy = candy-move    
            else:
                if move <= candy:
                    candy = candy-move
                    if candy == 0:
                        print('Вы победили!')
                        break   
                else:
                    print('Недопустимое количество взятых конфет, Вы хотите взять больше, чем осталось, попробуйте еще раз! ')  
                    move=int(input())
                    if move == candy:
                        print('Вы победили!')
                        break                        
    
                      
    return ConversationHandler.END                                                          # диалог закончен

def cancel(update,context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!')
 
# обучаем бота

start_handler = CommandHandler('start', start)                                              # если человек напишет start, то он запустит функцию старт
message_handler = MessageHandler(Filters.text, select_bot)
mes_man_handler = MessageHandler(Filters.text, select_man)
mes_canc_handler = MessageHandler(Filters.text, cancel)

# обработка событий
conv_handler = ConversationHandler(entry_points=[start_handler],                            # начальная точка
                                    states={A: [message_handler],
                                            B: [mes_man_handler]},
                                            fallbacks=[mes_canc_handler])                   # концовка

dispatсher.add_handler(conv_handler)          # пишем в скобках conv_handler (вместо start_handler), т.к. все ф-ции объеденены 
#dispatсher.add_handler(message_handler)   
#dispatсher.add_handler(mes_weather_handler)   
#dispatсher.add_handler(mes_canc_handler)     закомментировали, т.к. все описали выше conv_handler

updater.start_polling()   # начало бота
updater.idle()            # конец бота  
