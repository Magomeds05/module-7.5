import os

print('Путь:', os.getcwd())
if os.path.exists('first'):
    os.chdir('first')
else:
    os.mkdir('first')
    os.chdir('first')
for i in os.walk('.'):
    print(i)

print(os.path.join)

#Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
#Примените os.path.join для формирования полного пути к файлам.
#Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
#Используйте os.path.getsize для получения размера файла.
#Используйте os.path.dirname для получения родительской директории файла.
#Комментарии к заданию:
#Ключевая идея – использование вложенного for

#for root, dirs, files in os.walk(directory):
  #for file in files:
    #filepath = ?
    #filetime = ?
    #formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    #filesize = ?
    #parent_dir = ?
    #print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')