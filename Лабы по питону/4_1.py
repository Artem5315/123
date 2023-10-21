'''Требуется создать модуль с функциями для вычисления площадей прямоугольника, треугольника и круга:'''
import square

print("Выберите фигуру для вычисления площади:")
print("1. Прямоугольник")
print("2. Треугольник")
print("3. Круг")

choice = int(input("Введите номер фигуры: "))

if choice == 1:
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    area = square.rectangle(a, b)
    print("Площадь прямоугольника: ", area)
elif choice == 2:
    a = float(input("Введите длину основания: "))
    h = float(input("Введите высоту: "))
    area = square.triangle(a, h)
    print("Площадь треугольника: ", area)
elif choice == 3:
    r = float(input("Введите радиус круга: "))
    area = square.circle(r)
    print("Площадь круга: ", area)
else:
    print("Некорректный выбор фигуры")
