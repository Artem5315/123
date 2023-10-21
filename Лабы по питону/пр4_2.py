'''В7-В13: Вывести содержимое любой вашей папки в следующем виде (с
соответствующими отступами).
Дерево каталогов: Вывести в виде:
В ПАПКЕ – C:\delicious
ЕСТЬ ВЛОЖЕННАЯ ПАПКА – cats
ЕСТЬ ВЛОЖЕННАЯ ПАПКА – walnut
ЕСТЬ ФАЙЛ - spam.txt
В ПАПКЕ – С:\delicious\cats
ЕСТЬ ФАЙЛ – catnames.txt
ЕСТЬ ФАЙЛ – zophie.jpg
В ПАПКЕ – C:\delicious\walnut
ЕСТЬ ВЛОЖЕННАЯ ПАПКА – waffles
В ПАПКЕ – С:\delicious\walnut\waffles
ЕСТЬ ФАЙЛ - butter.txt'''

import os

def cmdir (n, a):
    for item in os.listdir(n):
        full_a = os.path.join(n, item)
        if os.path.isdir(full_a):
            print(f"{' ' * a}ЕСТЬ ВЛОЖЕННАЯ ПАПКА – {item}")
            cmdir(full_a, a + 4)
        else:
            print(f"{' ' * a}ЕСТЬ ФАЙЛ – {item}")

print(f"В ПАПКЕ – C:\\delicious")
cmdir("C:\\delicious", 4)
