#2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
#[12,'sadf',5643] ---> ['sadf'] ,[12,5643]


list0 = [12,'sadf',5643]
list_num = list(filter(lambda x: type(x) is int, list0))
print(list_num)

list0 = [12,'sadf',5643]
list_str = list(filter(lambda x: type(x) is str, list0))
print(list_str)


