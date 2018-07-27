from ebooklib import epub
from models import FanficData


def set_description(data: FanficData):
    content = ''' <body>
    <h1 class='omni-title'>''' + data.name + '''</b></h1>
    <h3 class= 'omni-subtitle'>by <em>''' + data.author.name + '''</em></h3>
    <br />
    <ul>
    <li><strong>Summary:</strong>''' + data.description + '''</li>
    <li><strong>Info:</strong>''' + data.info + '''</li>
          <li><strong>Fandom:</strong>''' + data.fandom + ''' </li>
      <li><strong>Source:</strong> <a href="''' + data.url + '''">''' + data.url + '''</a></li>
    </ul>
    </body>'''
    resp = epub.EpubHtml(title='Description', file_name="desc.xhtml")
    resp.content = content
    return resp

def create_epub(file_name: str, data: FanficData):
    book = epub.EpubBook()
    # name
    book.set_title(data.name)
    book.set_language('en')
    book.add_author(data.author.name)
    chapters = []
    for n, c in enumerate(data.chapters):
        chapter = epub.EpubHtml(title=c.name, file_name="chap_" + str(n) + ".xhtml")
        chapter.content = '<h3>' + c.name + '</h3>' + c.data
        book.add_item(chapter)
        chapters.append(chapter)
    book.toc = chapters
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    style = 'BODY {color: white;}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)
    desc = set_description(data)
    book.add_item(desc)
    book.spine = [desc, 'nav'] + chapters
    epub.write_epub(file_name, book, {})
