#Напишите программу, удаляющую из текста все слова, содержащие "абв".
#Пример:
#Привет Приабвет   приабев  приветабв
#Вывод:  Привет приабев

'''
with open("text2", "r", encoding='utf_8') as file:
    # print(file.read())
    res = list(map(str, file.readline().split()))
    print(res)                                          # по индексам
    for i in range(len(res)):
        if not "абв" in res[i] :
            print(res[i])

'''

with open("text2", "r", encoding='utf_8') as file:
    # print(file.read())
    res = list(map(str, file.readline().split()))       # по элементам
    print(res)
    for i in res:
        if not "абв" in i :
            print(i)            

