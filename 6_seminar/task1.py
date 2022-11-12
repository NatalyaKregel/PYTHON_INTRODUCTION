#Напишите программу вфчисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. Приоритет снадартный.
# Пример: 2+2 = 4, 1+2*3 = 7

#Приоритет стадартный:

def parse(s):                   # чтение текста и преобразование его в список
    result = []
    digit = " "
    for symbol in s:
        if symbol.isdigit():
            digit += symbol
        else:
            result.append(int(digit))   # если флоат = будет работать с вещественными числами
            digit = " "
            result.append(symbol)
    else:
        if digit:
            result.append(int(digit))
    return result

def calculate(lst):
    result = 0.0
    while "*" in lst:
        index = lst.index("*")                  # находим индекс ЗНАКА (третий сейчас)
        result = lst[index-1] * lst[index+1]    # берем соседние элементы от знака и умножаем и ложим в result
        lst = lst[:index-1] + [result] + lst[index+2:]  # создаем новый список, т.к. вместо 3*10 у нас 30
        #[12,'+',3,'*',10,'+',2]
        # [12,'+',30,'+',2]     берем срез до левой границы, прибавляем результат 30 и добавляем оставшуюся часть среза
    while "/" in lst:
        index = lst.index("/")
        result = lst[index-1] / lst[index+1]
        lst = lst[:index-1] + [result] + lst[index+2:]    
    while "+" in lst:
        index = lst.index("+")
        result = lst[index-1] + lst[index+1]
        lst = lst[:index-1] + [result] + lst[index+2:]
    while "-" in lst:
        index = lst.index("-")
        result = lst[index-1] - lst[index+1]
        lst = lst[:index-1] + [result] + lst[index+2:]    
    return result

s = "12+3*10+2"             # строка, но можно через импут, преобразовали строку в список [12,'x',3,'*',10,'+',2]
result = parse(s)

print(result)
print(calculate(result))


