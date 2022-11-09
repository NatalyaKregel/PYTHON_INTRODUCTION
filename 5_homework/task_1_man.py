# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота
# *** b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

print("-" * 70)
print('Здравствуйте! Вас приветствует игра "Забери все конфеты!" ')
print('Основные правила игры: за один ход мы можем взять не более 28 конфет, ')
print('Итак, начнём!')
print("-" * 70)
from random import randint

candy=int(2021)
max_candy = int(28)
bot_move = max_candy

for i in range(candy,0,-1):                                                                  
    if i % 2 == 1:
        print("Человек берет конфет: ", end='')
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
            #ost = candy
            if move <= candy:
                candy = candy-move
                print('Осталось -', candy)
                if candy==0:
                    print('Вы победили!')
                    break   
            else:
                print('Недопустимое количество взятых конфет, Вы хотите взять больше, чем осталось, попробуйте еще раз! ')  
                print('Осталось -', candy)   
                move=int(input())
                if move==candy:
                    print('Вы победили!')
                    break  
                     
                     
    if i % 2 == 0:
        print("Бот берет конфет: ", end='')
        if candy < max_candy:
            bot_move=candy

        move2 = randint(1,bot_move)
        print(move2)
        candy = candy-move2
        print('Осталось -', candy)


        if candy == 0:
            print('Победил БОТ!')
            break 

        