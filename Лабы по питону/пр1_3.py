while True:
    a = int(input("Введите значение для переменной a: "))
    b = int(input("Введите значение для переменной b: "))

    # Операция "И"
    c = a and b
    print("a И b =", c)

    # Операция "ИЛИ"
    d = a or b
    print("a ИЛИ b =", d) 

    choice = input("Хотите продолжить работу с программой? (y/n): ")
    if choice.lower() == 'n':
        print("Работа программы завершена.")
        break
  
