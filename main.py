import os

MONTH = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
         'Декабрь']

PATH_TO_DIR = input("Введите путь к папке с фотографиями: ")
os.chdir(PATH_TO_DIR)
os.mkdir('2023')
os.chdir('2023')
for i in range(len(MONTH)):
    os.mkdir(f"{i + 1}.{MONTH[i]}")
