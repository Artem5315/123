#В7-В13: Получить копию прямоугольной области экрана (скриншот экрана) 150,150, 800, 800 с помощью функции grab() из модуля ImageGrab. Вывести на изображении сегодняшнюю дату.
from datetime import datetime
from PIL import ImageGrab, ImageDraw, ImageFont

# Получаем скриншот прямоугольной области экрана
image = ImageGrab.grab((150, 150, 800, 800))

# Создаем объект ImageDraw для рисования на изображении
draw = ImageDraw.Draw(image)

# Добавляем текущую дату на изображение
font = ImageFont.truetype('arial.ttf', 30)
date = datetime.now().strftime('%Y-%m-%d')
draw.text((10, 10), date, fill='black', font=font)

# Сохраняем изображение
image.save('output.png')
