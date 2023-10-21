print('Введите количество чисел в наборе')
n = int(input()) # вводим количество чисел в наборе
print('Введите набор чисел')
a = list(map(int, input().split())) # вводим сам набор чисел

first_zero = -1 # переменная для хранения индекса первого нуля
last_zero = -1 # переменная для хранения индекса последнего нуля

# ищем первый и последний нули в наборе
for i in range(n):
    if a[i] == 0:
        if first_zero == -1:
            first_zero = i
        else:
            last_zero = i
            break

# если первый и последний нули не найдены или они идут подряд, выводим 0
if first_zero == -1 or last_zero == -1 or first_zero == last_zero - 1:
    print(0)
else:
    s = 0
    # суммируем числа между первым и последним нулями
    for i in range(first_zero+1, last_zero):
        s += a[i]   
    print('Сумма чисел между нулями', s)
