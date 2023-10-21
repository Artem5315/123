#Задание 5 Создать новое изображение и, используя методы модуля ImageDraw библиотеки Pillow, изобразить различного рода фигуры и текст.
#Некоторые методы объекта ImageDraw описаны в файле «Модуль ImageDraw.pdf»

from PIL import Image, ImageDraw, ImageFont

# Создаем новое изображение
image = Image.new('RGB', (500, 500), 'white')

# Создаем объект ImageDraw для рисования на изображении
draw = ImageDraw.Draw(image)

# Рисуем прямоугольник
draw.rectangle((50, 50, 150, 150), fill='blue')

# Рисуем эллипс
draw.ellipse((200, 50, 300, 150), fill='red')

# Рисуем многоугольник
draw.polygon(((350, 50), (400, 50), (450, 100), (400, 150), (350, 150)), fill='green')

# Рисуем линию
draw.line((50, 200, 150, 300), fill='black', width=3)

# Добавляем текст
font = ImageFont.truetype('arial.ttf', 30)
draw.text((200, 250), 'Hello, World!', fill='black', font=font)

# Сохраняем изображение
image.save('output.png')
