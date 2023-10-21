string = input("Введите строку: ")
substring = input("Введите подстроку: ")

start = string.lower().find(substring.lower())
if start == -1:
 print("Подстрока не найдена")
else:
 end = start + len(substring) - 1
print("Подстрока найдена на позициях от", start, "до", end)
