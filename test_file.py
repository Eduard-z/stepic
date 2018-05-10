import os


print(os.getcwd())  # текущая папка
print(os.listdir())  # список файлов
print(os.listdir('.idea'))  # список файлов
print(os.path.exists('test.py'))  # существует
print(os.path.abspath('test.py'))  # путь

for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)
