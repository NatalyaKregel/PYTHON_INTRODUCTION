#Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке



n = int(input('Введите число Фибоначчи: '))
a, b = 1, 1
if (n==1):
    print(1)
elif (n==2): 
    print(1, 1)
else: 
    print(a, b, end=' ')       # вывод начала списка 1, 1
    for i in range(2,n):
        temp = a
        a = b
        b = temp + b
        print(b, end=' ')      # вывод остальных чисел списка от 2 до n