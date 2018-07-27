from datetime import date
from time import sleep
from urllib.parse import urljoin
import requests
from lxml import html, etree
from models import AuthorData, ChapterData, FanficData


def get_chapter_data(tree):
    chapter = ChapterData()
    chapter.data = etree.tostring(tree.xpath('//*[@id="storytextp"]')[0], pretty_print=True).decode('utf-8')
    if len(tree.xpath('//*[@id="chap_select"]/option[@selected]/text()')) == 0:
        chapter.name = "Chapter 1"
    else:
        chapter.name = str(tree.xpath('//*[@id="chap_select"]/option[@selected]/text()')[0]).split(' ', 1)[1]
    return chapter


def parse_chapters(url: str, tree):
    print("start parse chapters")
    if url.split('/').__len__() == 7:
        url = url.rsplit('/', 1)[0]
    if url.split('/').__len__() == 5:
        url = url + "/1"
    count = int(int(tree.xpath('count(//*[@id="chap_select"]/option)')) / 2)
    chapters = []
    if count == 0:
        return [get_chapter_data(tree)]
    for i in range(1, count + 1):
        sleep(1)
        print("|", sep='', end='', flush=True)
        chapters.append(
            get_chapter_data(
                html.fromstring(
                    requests.get(
                        urljoin(url, str(i))
                    ).text
                )
            )
        )
    print(' Done')
    return chapters


def get_size(data:str) -> int:
    n1 = data.split('Words: ')
    n2 = n1[1].split(' - Reviews:')[0].replace(',', '')


def parse(url: str):
    _page = requests.get(url)
    print('start parse url ', url)
    data = FanficData()
    tree = html.fromstring(_page.text)
    if len(tree.xpath('//*[@id="content_wrapper_inner"]/div/span[@class="gui_warning"]')) == 1:
        raise ValueError('not_found')
    data.name = tree.xpath('//*[@id="profile_top"]/b/text()')[0]
    data.author = AuthorData(
        name=tree.xpath('//*[@id="profile_top"]/a[1]/text()')[0],
        url=urljoin(url, tree.xpath('//*[@id="profile_top"]/a[1]/@href')[0]),
    )

    data.description = tree.xpath('//*[@id="profile_top"]/div/text()')[0]
    data.size = get_size(tree.xpath('//*[@id="profile_top"]/span[@class="xgray xcontrast_txt"]/text()')[1])
    data.updated = date.fromtimestamp(int(tree.xpath('//@data-xutime')[0]))
    data.created = date.fromtimestamp(int(tree.xpath('//@data-xutime')[-1]))
    data.chapters = parse_chapters(url, tree)
    return data


urls = ['https://www.fanfiction.net/s/2636963', 'https://www.fanfiction.net/s/13014791/1/Sakura-Blossoms']

print(parse(urls[0]).chapters[0])
