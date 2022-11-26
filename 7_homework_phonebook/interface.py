from data import get_data
from logger import export_csv, export_txt, import_contact

print('ДОБРО ПОЖАЛОВАТЬ В СПРАВОЧНИК КОНТАКТОВ!')
print('---------------------------------------- ')
print('Выберите действие, которое хотите сделать: ')
print('1. Записать в справочник новый контакт\n2. Вывести весь справочник на экран')
flag = int(input())
if flag == 1:
    a = get_data()
    export_txt(a) 
    export_csv(a)
elif flag == 2:
    print(import_contact())
else:
    print('Некорректные данные')
    