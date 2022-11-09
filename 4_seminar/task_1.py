#1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

import math
from random import random
N = 5
a = []
for i in range(N):
    b = int(random() * 20)    
    a.append(b)

print('Максимальное число списка: ', '%.f'% max(a))
print('Минимальное число списка: ', '%.f'% min(a))
print('Разница между максимальным и минимальным числами: ', round(max(a)-min(a)))



exit()
print('Введите строку состоящую из чисел')
n = str(input()).split()
print(n)
max = int(n[0])
min = int(n[0])
for i in (n):
    if int(i) > max:
        max = int(i)
    if int(i) <= min:
        min = int(i)
print(f'Максимальное число в строке = {max}, минимальное число в строке = {min}')



