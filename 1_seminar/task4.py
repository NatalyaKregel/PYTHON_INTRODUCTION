# Принимает дробь и показывает первое число после запятой, если введено целое число напишет НЕТ
 

print ('Введите дробное число: ')
a = input()
string = str(a)
if '.' in string:
    a = float(a)
    a = a * 10
    a = a % 10
    print(int(a))
else:
    print('нет')    