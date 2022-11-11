#3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
# 6782 -> 23
# 0.56 -> 11
#Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
'''
ВАРИАНТ 1:

print('Введите число:')
s = float(input())
result = sum(int(i) for i in str(s) if i.isdigit())
print('Сумма цифр введенного числа =', result)

ВАРИАНТ 2:
'''
print('Введите число:')
s = float(input())
print(sum(map(float, filter(str.isdigit, str(s)))))
#print('Сумма цифр введенного числа =', sum)