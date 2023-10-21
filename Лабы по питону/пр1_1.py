print("1-прямоугольник, 2-треугольник, 3-круг")
figure = input("Выберите фигуру: ")
 
if figure == '1':
    print("Длины сторон прямоугольника:")
    a = float(input("a = "))
    b = float(input("b = "))
    if a <= 0 or b <= 0:
        print("Ошибка: введены некорректные значения сторон")
    else:
        print("Площадь: %.2f" % (a * b))
elif figure == '2':
    print("Длины сторон треугольника:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    if a <= 0 or b <= 0 or c <= 0:
        print("Ошибка: введены некорректные значения сторон")
    else:
        p = (a + b + c) / 2
        from math import sqrt
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        print("Площадь: %.2f" % s)
elif figure == '3':
    r = float(input("Радиус круга R = "))
    if r <= 0:
        print("Ошибка: введено некорректное значение радиуса")
    else:
        from math import pi
        print("Площадь: %.2f" % (pi * r ** 2))
else:
    print("Ошибка ввода")
