from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint

bot = Bot(token='5712662084:AAEHqQVWAJNeLaa7j8tZdOcxj59Dg5ZzYq4')
updater = Updater(token='5712662084:AAEHqQVWAJNeLaa7j8tZdOcxj59Dg5ZzYq4')
dispatcher = updater.dispatcher               # находится мозг нашего бота

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Сколько конфет вы берете?')

def bet(update, context):                     # cтавка
    text = int(update.message.text)
    a = select_man
    b = select_bot
    result = win(a,b,text)
    context.bot.send_message(update.effective_chat.id, a)
    context.bot.send_message(update.effective_chat.id, b)
    context.bot.send_message(update.effective_chat.id, f'Победил {result}')


def select_man (candy,move):
    candy=int(200)
    max_candy = int(28)
    for i in range(candy,0,-1):                                                                  
        if i % 2 == 1:
        #print("Человек берет конфет: ", end='')
            move = int(input())
            if candy > max_candy:
                if move <= max_candy:
                    candy = candy-move
                    print('Осталось -', candy) 
                else:
                    print('Недопустимое количество взятых конфет, максимально можно взять 28, попробуйте еще раз! ')
                    move=int(input())
                    if move <= max_candy:
                        candy = candy-move    
                        print('Осталось -', candy)  
            else:
                if move <= candy:
                    candy = candy-move
                    print('Осталось -', candy)
                    if candy == 0:
                        print('Вы победили!')
                        break   
                else:
                    print('Недопустимое количество взятых конфет, Вы хотите взять больше, чем осталось, попробуйте еще раз! ')  
                    print('Осталось -', candy)   
                    move=int(input())
                    if move == candy:
                        print('Вы победили!')
                        break                        
def select_bot (candy, move2):
    candy=int(200)
    max_candy = int(28)
    bot_move = max_candy        
    if i % 2 == 0:
        print("Бот берет конфет: ", end='')
        if candy < max_candy:
            bot_move = candy
            move2 = randint(1,bot_move)
            print(move2)
            candy = candy - move2
            print('Осталось -', candy)

def win (candy,move,move2):
    if move == candy:
        print('Победил человек')
    elif move2 == candy:
        print('Победил бот')
    return     
    
            
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, bet)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
