'''Суммировать вводимые числа, среди которых нет нулевых. При
вводе нуля обеспечить вывод текущего значения суммы. При вводе
числа 99999 закончить работу.'''
def sum_without_zeros():
    sum = 0
    while True:
        number = int(input("Введите число: "))
        if number == 0:
            print("Текущая сумма:", sum)
        elif number == 99999:
            print("Работа завершена.")
            return sum
        else:
            sum += number
