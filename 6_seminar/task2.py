# Дана последовательность чисел. Получить список уникльных элементов последовательности. 
# Без использования count
'''
list1 = [1, 2, 7, 9, 22, 3, 5, 1, 5, 3, 10]
list2 = []
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
    else:
        list2.remove(list1[i])    
print(list2)       
'''

# от Никиты

def list2(data):
    result = []
    result_new = []
    for el in data:
        if el not in result and el not in result_new:
            result.append(el)
            result_new.append(el)
        elif el in result:
            result.remove(el)
    print(result_new)       # result_new показывает список чисел, с которыми он работал
    return sorted(result)   # result список уникальных чисел

num = [1,2,3,5,1,5,6,1,1,7]
print(f'Исходная последовательность: {num}') 
print(f'Отсортированный список уникальных элементов: {list2(num)}') 

