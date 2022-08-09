import requests
from bs4 import BeautifulSoup
import time
import os
import math

url = 'https://wallscloud.net/ru/category/textures'
dpi = '1920x1080'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.74'
}

res = requests.get(url, headers=headers).content
soup = BeautifulSoup(res, 'html.parser')  # делаем суп

# Определение общего числа обоев
page_title = soup.find('div', class_='page-title')
count_picture = page_title.find('small').text
count_picture = int(count_picture.split()[0])
print(count_picture)

name_title = page_title.find('h1').text.strip(' \n')
path_to_file = f'M:\\Рисунки\\ОБОИ\\Wallscloud\\{name_title}'

# Определение количества страниц с картинками
count_pages = math.ceil(count_picture / 35)  # т.к. на каждой странице располагаются по 35 картинок
print(count_pages)


def create_dir(path_to_file: str) -> None:
    """Создание папки для загрузки файлов картинок"""
    if not os.path.exists(path_to_file):
        os.makedirs(path_to_file)
        print(f'Создана папка {path_to_file} для записи файлов')
    else:
        print(f'Папка {path_to_file} уже существует. Продолжаем работу программы.')


# Создание папки загрузки
create_dir(path_to_file)

count = 0
dict_repeat = {}  # словарь для файлов с повторяющимися названиями
for i in range(count_pages):
    url_new = f'{url}?page={i + 1}'  # адрес следующих страниц картинок
    time.sleep(0.5)
    res = requests.get(url_new, headers=headers).content
    soup = BeautifulSoup(res, 'html.parser')  # делаем суп

    # Поиск ссылок на картинки
    links = soup.find('div', class_='grid_container walls_data').find_all('div', class_="pr")
    for link in links:
        ref = link.find('a', class_='wall_link').get('href')  # поиск ссылки на картинку
        ref_download = f'{ref}/{dpi}/download'  # формирование ссылки для загрузки с заданным расширением dpi
        name_ref = link.find('div', class_='transition name').text.strip('\n')  # поиск и формирование имени картинки
        time.sleep(1)
        byte = requests.get(ref_download).content  # загрузка картинки
        count += 1

        filename = f'{path_to_file}\\{name_ref}.jpeg'
        if os.path.exists(filename):
            dict_repeat[name_ref] = dict_repeat.get(name_ref, 0) + 1
            filename = f'{path_to_file}\\{name_ref}_{dict_repeat[name_ref]}.jpeg'

        with open(filename, 'wb') as f:
            f.write(byte)  # сохранение картинки на диск
        print(f'№{count} Запись файла {os.path.basename(filename)} прошла успешно!')

print(f'Загрузка окончена! Скачано {count} файлов')
