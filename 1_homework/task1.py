#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

print('Введите число от 1 до 7: ')
a=int(input())
if (a>0 and a<=5):
    print('нет')
elif (a>5 and a<=7):
    print('да')
elif a>7:
    print('Вы ввели неверное число')    