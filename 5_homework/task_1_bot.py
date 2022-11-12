# a) Добавьте игру против бота

print('Здравствуйте! Вас приветствует игра "Забери все конфеты!" ')
print('Основные правила игры: за один ход мы можем взять не более 28 конфет, ')
print('Итак, начнём!')

from random import randint

candy=int(2021)
max_candy = int(28)
bot_move = max_candy

for i in range(candy,0,-1):
    if i % 2 == 1:
        print("Бот 1 берет конфет: ", end='')
        if candy < max_candy:
            bot_move=candy

        move2 = randint(1,bot_move)
        print(move2)
        candy = candy-move2
        print('Осталось -', candy)

        if candy == 0:
            print('Победил 1 БОТ!')
            break               
                     
    if i % 2 == 0:
        print("2 Бот берет конфет: ", end='')
        if candy < max_candy:
            bot_move=candy

        move2 = randint(1,bot_move)
        print(move2)
        candy = candy-move2
        print('Осталось -', candy)

        if candy == 0:
            print('Победил 2 БОТ!')
            break 

        

        