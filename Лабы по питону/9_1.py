#Задание1 Вариант 10 Создать изображение и покрыть одинаковыми изображениями всю об¬ласть основного изображения:
from PIL import Image

# Открываем изображение
image = Image.open('1.png')

# Получаем размеры изображения
width, height = image.size

# Создаем новое изображение с такими же размерами как исходное
new_image = Image.new('RGB', (width, height))

# Уменьшаем исходное изображение в 4 раза
small_image = image.resize((width // 4, height // 4))

# Добавляем уменьшенные копии изображения на новое изображение
for i in range(4):
    for j in range(4):
        new_image.paste(small_image, (i * width // 4, j * height // 4))

# Сохраняем новое изображение
new_image.save('output.png')
