# Задание 2 Добавить логотип в нижний правый угол каждого изображения, находящегося в папке, и изменить размеры изображения так, чтобы они вписывались в квадрат 500*500.
import os
from PIL import Image

# Константы
LOGO_FILENAME = 'logo.png'
SQUARE_FIT_SIZE = 500

# Открываем изображение логотипа
logo = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo.size
logo = logo.convert('RGBA')

# Создаем папку для хранения изображений с логотипами
os.makedirs('withLogo', exist_ok=True)

# Обходим все файлы в рабочем каталоге
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue  # Пропускаем неизображения и сам логотип

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

    # Добавляем логотип в правый нижний угол изображения
    image.paste(logo, (width - logo_width, height - logo_height), logo)

    # Сохраняем измененное изображение в папке withLogo
    image.save(os.path.join('withLogo', filename))
