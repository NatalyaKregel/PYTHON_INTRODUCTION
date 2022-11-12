#1) В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
#Пример: 1 2 3 5 6 7
#Вывод: 4
with open("file.txt", "r") as file:
    print(file.readline())
    #list = list(file.readline())
    # print(list)
    spisok = list(map(int, (file.readline().split())))
    print(spisok)
    for i in range(1, len(spisok)):
        if spisok[i] - 1 != spisok[i-1]:
            print(spisok[i] - 1)

            


