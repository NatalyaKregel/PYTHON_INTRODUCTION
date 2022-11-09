# На вход принимает число N и выводит все числа от -N до N.
 
n = int (input('Введите число: '))
for number in range(-n, n+1):
    print(number) 