#Есть ли в списке число?

list = ['строка 1', 'строка', 'строка 3', 'строка', '13']
num = input('Введите число: ')
count = 0
for i in list:
    if num in i:
        print('Да есть')
        count = 1
        break
if count == 0:
    print('Нет')

