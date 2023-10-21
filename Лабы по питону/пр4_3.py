import os
import zipfile

def create_backup(folder_path):
    # Получаем имя папки
    folder_name = os.path.basename(folder_path)
    # Создаем имя архива
    zip_name = f"{folder_name}_backup.zip"
    # Создаем полный путь к архиву
    zip_path = os.path.join("D:\\копии на питоне с комментариями", zip_name)
    # Создаем zip-архив
    with zipfile.ZipFile(zip_path, "w") as zip_file:
        # Обходим все файлы и подпапки в указанной папке
        for root, dirs, files in os.walk(folder_path):
            # Добавляем каждый файл в архив
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zip_file.write(file_path, arcname)
    print(f"Резервная копия папки {folder_name} создана в архиве {zip_name}")
