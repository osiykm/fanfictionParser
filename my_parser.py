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
    url = url.replace("\n", "")
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


def get_text(param):
    resp = ""
    for t in param:
        resp = resp + t
    return resp


def parse(url: str):
    _page = requests.get(url)
    print('start parse url ', url)
    data = FanficData()
    data.url = url
    tree = html.fromstring(_page.text)
    if len(tree.xpath('//*[@id="content_wrapper_inner"]/div/span[@class="gui_warning"]')) == 1:
        raise ValueError('not_found')
    data.name = tree.xpath('//*[@id="profile_top"]/b/text()')[0]
    data.author = AuthorData(
        name=tree.xpath('//*[@id="profile_top"]/a[1]/text()')[0],
        url=urljoin(url, tree.xpath('//*[@id="profile_top"]/a[1]/@href')[0]),
    )
    data.fandom = tree.xpath('//*[@id="pre_story_links"]/span/a/text()')[-1]
    data.description = tree.xpath('//*[@id="profile_top"]/div/text()')[0]
    data.info = get_text(tree.xpath('//span[@class="xgray xcontrast_txt"]/text()'))
    data.chapters = parse_chapters(url, tree)
    return data

