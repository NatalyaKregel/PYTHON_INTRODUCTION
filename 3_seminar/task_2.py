# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.  
list = ["qwe", "asd", "zxc", "qwe", "ertqwe"] 
elem = input('Введите число: ') 
count = 0 
index = 0 
for i in list:     
    if elem == i:         
        count += 1     
    if count == 2:         
        print(index)         
        break     
    index += 1 
if count<2:     
    print('Нет второго вхождения')

exit()
или

def find_second_index(lst, substr):    
     if lst.count(substr) < 2:        
        return 'Нет второго вхождения'     
        return lst.index(substr, lst.index(substr)+1)            
        tests = [     
            [["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe"],     
            [["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "йцу"],     
            [["йцу", "фыв", "ячс", "цук", "йцукен"], "йцу"],
            [["123", "234", 123, "567"], "123"],
            [[], "123"]
        ]

for test, substr in tests:
    print(find_second_index(test, substr))


# от преподавателя!
# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.  
spisok = ['строка1', 'строка2', 'строка3', 'строка1']   
spisok = ['строка2', 'строка3', 'строка1'] 
find_str = 'строка1' 
if spisok.count(find_str) < 2:     
    print(f'Второго вхождения строки {find_str} нет в заданном списке')
else:     
    spisok.remove(find_str)              # удаляем первое вхождение в список     
print(spisok.index(find_str) + 1)    # ищем строку в оставшемся списке и прибавляем тот индекс, который удалили

