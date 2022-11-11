#2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
#[12,'sadf',5643] ---> ['sadf'] ,[12,5643]


#n = [12,'sadf',5643]
#print(*list(filter(lambda x: x.isdigit(),int(n))))
'''
s = "12,sadf,5643"
import re
s1 = re.sub("[0-9]", "", s)
print(s1)
s2 = "".join(c for c in s if  c.isdecimal())
print(s2)
'''

num = ['12','sadf','5643']
f = filter(lambda x: x.replace('.', '').isdigit(), num)
f = list(f) 
print(f)

s = [12,'sadf',5643]
ss = list(filter(None, s))
print(ss)

                   

