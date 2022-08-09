import requests
from bs4 import BeautifulSoup
import time
import os


class Parser_foto:
    def __init__(self, url):
        self.url = url.strip('/')
        self.dom = self.url.split('//')[1].split('/')[0]
        self.dpi = self.url.split('/')[-2]
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.74'
        }

    def download_to_file(self, name='pic.html'):
        """Сохранение страницы html в файл"""
        res = requests.get(self.url, self.headers).content
        with open(name, 'w') as f:
            f.write(res)

    def soup_from_file(self, name_file="pic.html"):
        """Парсинг из ранее записанного файла html"""
        with open(name_file, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
            return soup

    def soup_process(self):
        """"""
        res = requests.get(self.url, self.headers).content
        soup = BeautifulSoup(res, 'html.parser')
        return soup

    def makedir(self):
        """Создание папки для загрузки файлов картинок"""
        self.path_to_file = f'D:\\Pic2\\{self.dpi}_{self.url.split("/")[-1]}'  # генерируется имя папки для загрузки по выбранной теме
        if not os.path.exists(self.path_to_file):
            os.makedirs(self.path_to_file)
            print(f'Создана папка {self.path_to_file} для записи файлов')
        else:
            print(f'Папка {self.path_to_file} уже существует. Продолжаем работу программы.')

    def download(self, soup):
        """Скачивание файлов с сайта"""
        # Определение количества страниц на которых находятся картинки
        pagin = soup.find('ul', class_='pagination')  # поиск по тегу <ul>, который содержит class pagination
        link = [i.get('href') for i in pagin.find_all('a')]
        a = [i[:-1].split('/')[-1] for i in link]
        pages = max(map(int, a))
        print(pages)
        self.pages = int(input(f'Сколько надо просмотреть страниц из {pages}?  '))

        #Загрузка файлов на диск
        self.count = 0  # количество скачанных файлов
        for i in range(1, self.pages + 1):
            time.sleep(0.1)
            res = requests.get(f'{self.url}/{i}', self.headers).content
            soup_link_foto = BeautifulSoup(res, 'html.parser')  # соуп по каждому фото
            # Список тегов с ссылками на картинки на странице
            a = soup_link_foto.find_all('a', class_='oneimage_a normal')
            lst_ref = [i.get('href') for i in a]
            for i in lst_ref:
                num = i.split('/')[-1].split('.')[0]
                ref = f'https://storge.pic2.me/download/{self.dpi}/{num}.jpeg'
                print(ref)
                byte = requests.get(ref).content
                with open(f'{self.path_to_file}\\{num}.jpeg', 'wb') as f:
                    f.write(byte)
                    self.count += 1
                    print(f'{self.count} Запись файла {num}.jpeg прошла успешно!')

    def get_pages(self):
        """Количество скачанных файлов"""
        return self.count


def main():
    url = input('Введите адрес страницы: ') #
    if 'https://pic2.me/resolusion/' not in url:
        url = 'https://pic2.me/resolusion/1920x1080/abstraction' #для примера
    picture = Parser_foto(url)
    soup = picture.soup_process()
    picture.makedir()
    picture.download(soup)
    print(f'Загрузка окончена! Скачано {picture.get_pages()} файлов')


if __name__ == '__main__':
    main()
