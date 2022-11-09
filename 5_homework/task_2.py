print("*" * 22)
print(" Игра Крестики-нолики ")
print( "*" * 22)

board = list(range(1,10))

def draw_board(board):                                                           # создание поля для игры
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def input_step(cross_or_zero):                                                   # функция для ввода Х или 0
   valid = False
   while not valid:
      player_answer = input("Ход игрока: " + cross_or_zero +"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:                              # проверяем введенное число попадает в разрешенный диапозон
         if(str(board[player_answer-1]) not in "XO"):                            # вторая проверка, запрашиваемая клетка пустая?
            board[player_answer-1] = cross_or_zero                               # если да, вносим Х или 0
            valid = True
         else:
            print("Клетка занята! Попробуйте еще раз!")
      else:
        print("Некорректный ввод. Возможное число от 1 до 9")

def check_win(board):                                                                        # функция на проверку выигрышнй позиции
   win_position = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))   # проверяем возможные комбинации
   for step in win_position:
       if board[step[0]] == board[step[1]] == board[step[2]]:
          return board[step[0]]
   return False

def basic(board):                                                                # основная функция игры:
    counter = 0
    win = False
    while not win:
        draw_board(board)                                                        # вызов функции - поле игры
        if counter % 2 == 0:
           input_step("X")                                                       # если ход четный, вводим Х
        else:
           input_step("O")                                                       # если ход четный, вводим 0
        counter += 1
        if counter > 4:                                                          # если ходов сделано более 4 вызываем функции на проверку выигрышной позиции
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:                                                        # если ходов сделано 9 и неопределена победа - ничья
            print("Ничья!")
            break
    draw_board(board)                                                           # вызов функции - поле игры 
basic(board)                                                                    # вызов основной функции 