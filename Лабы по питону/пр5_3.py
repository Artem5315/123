import math
def solve_quadratic_equation():
    try:
        a = float(input("Введите коэффициент a: "))
        b = float(input("Введите коэффициент b: "))
        c = float(input("Введите коэффициент c: "))

        # Рассчитываем дискриминант
        discriminant = b**2 - 4*a*c

        # Проверяем, есть ли решение
        if discriminant < 0:
            raise ValueError("Уравнение не имеет решения")

        # Рассчитываем корни уравнения
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)

        print("Корни уравнения {}x^2 + {}x + {} = 0:".format(a, b, c))
        print("x1 =", x1)
        print("x2 =", x2)

    except ValueError as e:
        print("Ошибка:", e)

solve_quadratic_equation()
