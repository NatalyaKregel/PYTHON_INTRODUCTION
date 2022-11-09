#2) Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#Примеры:
#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90

#import numbers


numbers = []
for i in range(5):
    number = int(input('Введите число: '))
    numbers.append(number)
print('Максимальное число=', max(numbers))
