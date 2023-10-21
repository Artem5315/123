#Задание 4 Применить к своему изображению любой из стандартных фильтров библиотеки Pillow.
import os
from PIL import Image, ImageFilter

# Константы
SQUARE_FIT_SIZE = 500

# Создаем папку для хранения изображений с фильтром
os.makedirs('withFilter', exist_ok=True)

# Обходим все файлы в рабочем каталоге
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')):
        continue  # Пропускаем неизображения

    # Открываем изображение
    image = Image.open(filename)
    width, height = image.size
    image = image.convert('RGB')

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

    # Добавляем фильтр к изображению
    image = image.filter(ImageFilter.BLUR)

    # Сохраняем измененное изображение в папке withFilter
    image.save(os.path.join('withFilter', filename))
