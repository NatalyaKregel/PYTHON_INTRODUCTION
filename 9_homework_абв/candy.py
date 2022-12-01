from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint

bot = Bot(token='5712662084:AAEHqQVWAJNeLaa7j8tZdOcxj59Dg5ZzYq4')
updater = Updater(token='5712662084:AAEHqQVWAJNeLaa7j8tZdOcxj59Dg5ZzYq4')
dispatcher = updater.dispatcher             # находится мозг нашего бота

start = 0
A = 1
move = 2
move2 = 3
win_bot = 4

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет!\nДавай поиграем в игру: кто заберет последнюю конфету тот и победил.')
    context.bot.send_message(update.effective_chat.id, 'Сколько конфет ты берешь?')
    return start

def start_candy(update, context):           #условие игры
    candy = int(2021)
    max_candy = int(28)
    context.bot.send_message(update.effective_chat.id, f'За один ход можно взять не более {max_candy} конфет')
    return A

def who_first(update, context):
    global complexity
    context.bot.send_message(update.effective_chat.id, 'Сейчас определим, кто будет ходить первым')
    for i in range(3, 0, -1):  
        context.bot.send_message(update.effective_chat.id, i)
    first_player = randint(0, 1)
    if first_player:
        context.bot.send_message(update.effective_chat.id, 'ТЫ ходишь первым!')
        return move
    else:
        context.bot.send_message(update.effective_chat.id, 'Я хожу первым!')
        select_bot(update, context)
        return move

def select_man (update, context,max_candy):
    global start_candy
    global num_start
    chislo = update.message.text
    for i in range(28,0,-1):                                                                  
        if i % 2 == 1:
            if chislo.isdigit():
                chislo = int(chislo)
            else:
                context.bot.send_message(update.effective_chat.id, f'Введены не верные данные')
                return move

    if chislo > max_candy or chislo <= 0 or chislo > num_start:
        context.bot.send_message(update.effective_chat.id, f'Введены не верные данные')
        return move

    num_start -= chislo
    context.bot.send_message(update.effective_chat.id, f'Осталось {num_start}')

    if num_start > 0:
        select_bot(update, context)
    else:
        win_man(update, context)
        return ConversationHandler.END
'''        
    for i in range(candy,0,-1):                                                                  
        if i % 2 == 1:
            move = int(input())
            if candy > max_candy:
                if move <= max_candy:
                    candy = candy-move 
                else:
                    context.bot.send_message(update.effective_chat.id, f'Недопустимое количество взятых конфет, максимально можно взять 28, попробуйте еще раз! ')
                    move = int(input())
                    if move <= max_candy:
                        candy = candy-move    
                        context.bot.send_message(update.effective_chat.id, f'Осталось {start_candy}')
            else:
                if move <= candy:
                    candy = candy-move
                    context.bot.send_message(update.effective_chat.id, f'Осталось {start_candy}')
                    if candy == 0:
                        break   
                else:
                    context.bot.send_message(update.effective_chat.id, f'Недопустимое количество взятых конфет, максимально можно взять 28, попробуйте еще раз! ')
                    context.bot.send_message(update.effective_chat.id, f'Осталось {start_candy}')
                    move=int(input())
                    if move == candy:
                        break      
    #return ConversationHandler.END
'''
def select_bot (update, context,candy,max_candy):
    for i in range(candy,0,-1):         
        if i % 2 == 0:
            if candy < max_candy:
                bot_move = candy
                move2 = randint(1,bot_move)
                context.bot.send_message(update.effective_chat.id, f'Я взял {move2}')
                context.bot.send_message(update.effective_chat.id, f'Осталось {start_candy}')
                return select_man
                        
def win_man (update, context):
    context.bot.send_message(update.effective_chat.id, f'Поздравляю!!!Ты победил!!!')

def win_bot (update, context):
        context.bot.send_message(update.effective_chat.id, f'Я победил!!!')  
         
def cancel_bot(update, context):
    context.bot.send_message(update.effective_chat.id, 'Пока!') 
    return ConversationHandler.END
    
def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Пока!')        
            
start_handler = CommandHandler('start', start)
start_candy_handler = MessageHandler(Filters.text, start_candy)
select_man_handler = MessageHandler(Filters.text, select_man)
select_bot_handler = MessageHandler(Filters.text, select_bot)
win_bot_handler = MessageHandler(Filters.text, cancel_bot)
mes_candy_handler = MessageHandler(Filters.text, cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={start: [start_candy_handler],
                                           A: [start_candy_handler],
                                           move: [select_man_handler],
                                           move2: [select_bot_handler],
                                           win_bot: [win_bot_handler]},
                                   fallbacks=[mes_candy_handler])

start_handler = MessageHandler(Filters.text, start)
dispatcher.add_handler(start_handler)          

updater.start_polling()                       
updater.idle()                                