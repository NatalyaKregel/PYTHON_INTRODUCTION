#Найти Максимальный элемент в списке из 5 элементов. (Не используя встроенные функции max())
#*Пример*
#Ввод: 3 -6 10 23 -14
#Ответ: 23

#numbers = []
#for i in range(5):
#    number = int(input('Введите число:'))
#    numbers.append(number)
#max = numbers[0]
#if max < numbers[1]:
#    max = numbers[1]
#if max < numbers[2]:
#    max = numbers[2]
#if max < numbers[3]:
#    max = numbers[3]
#if max < numbers[4]:
#    max = numbers[4]
#print('максимальное число = ', max)


n = [-23,1,41,2,3]
max = n[0]
for i in range(1,5):
    if max < n[i]:
        max = n[i]
print(max)        
