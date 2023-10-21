'''Вставьте нужную информацию в указанных местах в файле
coder for st.py. Программа должна вывести таблицу истинности шифратора &quot;4 в 2&quot;.'''
# Функция для вычисления значения выражения
def calc_expr(a, b, c, d):
    return ((a + b) % 2 == c) and ((b + c) % 2 == d)

# Вывод заголовка таблицы
print("A\tB\tC\tD\t4 в 2")
print("-" * 40)

# Обходим все возможные комбинации значений A, B, C и D
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                # Вычисляем значение выражения
                result = calc_expr(a, b, c, d)
                # Выводим строку таблицы
                print(f"{a}\t{b}\t{c}\t{d}\t{int(result)}")
