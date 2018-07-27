from config import urls_file

if __name__ == '__main__':
    urls = open(urls_file, 'r').readlines()
    for url in urls:


