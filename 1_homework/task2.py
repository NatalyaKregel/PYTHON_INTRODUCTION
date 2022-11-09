# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# Примечание: Используйте знания об Алгебра Логике, вы должны перебрать все возможные комбинации значений X, Y, Z (принимают значения 0 или 1)

print("X Y Z")               # заглавие таблицы истинности
# перебор возможных комбинаций с помощью вложенных циклов for: 
for X in range(0, 2):
	for Y in range(0, 2):
		for Z in range(0, 2):
			result = not (X or Y or Z) == (not X) and (not Y) and (not Z)
			print(X, Y, Z, result)