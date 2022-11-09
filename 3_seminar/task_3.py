# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.  

import time  
def get_rand(x, y):     
    scope = y - x                            # 20     
    print(time.time())        
    result = int(time.time()*1000) % scope   #1665771196939   --- 19
    return result + x
   
print(get_rand(80, 100))
print(get_rand(20, 30))
print(get_rand(80, 100))


exit()
или

import time   
def my_randint(start, stop):     
    numbers = [i for i in range(start, stop + 1)]     
    print(numbers)     
    time_stamp = time.time()     
    print(time_stamp)     
    rand_num = int((time_stamp - int(time_stamp)) * 1000)     
    rand_index = rand_num % len(numbers)
    return numbers[rand_index]

print(my_randint(int(input()), int(input())))
