# Download-wallpapers

В файле Parser_wallscloud_net.py размещен простой скрипт для автоматизированного скачивания файлов картинок для обоев рабочего стола с сайта wallscloud.net. Программа посуществляет скачивание файлов в формате jpeg в папку. Папка для загрузки создается автоматически программой.

Программа Parser_foto_class.py позволяет скачивать файлы картинок с сайта pic2.me. Для парсинга сайта в данной программе реализован класс Parser_foto (может использоваться, как полноценная программа, так и отдельным модулем) с набором методов, которые позволяют проводить  сохранение страницы html в файл, проводить парсинг ранее записанного файла html, создают автоматически папки для загрузки файлов картинок, определяют количество страниц на которых находятся картинки и предоставляет на выбор пользователю, необходимое количество страниц для обработки, осуществляют скачивание файлов в формате jpeg на жесткий диск, а также на всех этапах парсинга осуществляется сопровождение в виде сообщений в консоль.

В скриптах использованы следующие модули и библиотеки: requests, BeautifulSoup, time, math, os.
