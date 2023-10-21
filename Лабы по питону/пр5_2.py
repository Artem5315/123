import random
import tkinter as tk

dictionary = {
    "apple": "яблоко",
    "banana": "банан",
    "carrot": "морковь",
    "dog": "собака",
    "elephant": "слон"
}

# создаем окно приложения
root = tk.Tk()
root.title("Игра в слова")

# выбираем случайное слово из словаря
word = random.choice(list(dictionary.keys()))

# функция для проверки ответа пользователя
def check_answer():
    translation = entry.get()
    if translation == dictionary[word]:
        result_label.config(text="Правильно!")
    else:
        result_label.config(text="Неправильно. Правильный ответ: '{}'".format(dictionary[word]))

# создаем элементы интерфейса
word_label = tk.Label(root, text=word, font=("Arial", 24))
word_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 24))
entry.pack(pady=10)

button = tk.Button(root, text="Проверить", font=("Arial", 24), command=check_answer)
button.pack(pady=10)

result_label = tk.Label(root, font=("Arial", 24))
result_label.pack(pady=20)

# запускаем цикл обработки событий
root.mainloop()
