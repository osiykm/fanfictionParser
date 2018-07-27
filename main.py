from config import URLS_FILE, SAVE_FOLDER

from epub import create_epub
import my_parser

if __name__ == '__main__':
    urls = open(URLS_FILE, 'r').readlines()
    for url in urls:
        book = my_parser.parse(url=str(url))
        create_epub(SAVE_FOLDER + '/' + book.name.replace(" ", "_") + ".epub", book)
