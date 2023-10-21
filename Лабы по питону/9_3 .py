#Задание 3
#Изменить предыдущее задание таким образом, чтобы вместо картинки-логотипа во все изображения в левый верхний угол добавлялся текст, введенный пользователем.

import os
from PIL import Image, ImageDraw, ImageFont

# Константы
SQUARE_FIT_SIZE = 500
TEXT = input("Введите текст")
FONT = ImageFont.truetype('arial.ttf', 20)

# Создаем папку для хранения изображений с текстом
os.makedirs('withText', exist_ok=True)

# Обходим все файлы в рабочем каталоге
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')):
        continue  # Пропускаем неизображения

    # Открываем изображение
    image = Image.open(filename)
    width, height = image.size

    # Проверяем, не превышает ли ширина или высота изображения 500 пикселей
    if width > SQUARE_FIT_SIZE or height > SQUARE_FIT_SIZE:
        # Уменьшаем изображение
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Изменяем размер изображения
        image = image.resize((width, height))

    # Создаем объект ImageDraw для рисования на изображении
    draw = ImageDraw.Draw(image)

    # Добавляем текст в левый верхний угол изображения
    draw.text((0, 0), TEXT, fill='black', font=FONT)

    # Сохраняем измененное изображение в папке withText
    image.save(os.path.join('withText', filename))
