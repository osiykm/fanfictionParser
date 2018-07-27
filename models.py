from datetime import date
from typing import List


def _auto_str(cls):
    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )

    cls.__str__ = __str__
    return cls


@_auto_str
class ChapterData:
    def __init__(self, name: str = "", data: str = ""):
        self.name = name
        self.data = data


@_auto_str
class AuthorData:
    def __init__(self, name: str = "", url: str = ""):
        self.name = name
        self.url = url


Chapters = List[ChapterData]


@_auto_str
class FanficData:
    def __init__(self, name: str = "", author: AuthorData = AuthorData(), description: str = "", info: str = "",
                 fandom: str = "", url: str = "", chapters: Chapters = ()):
        self.name = name
        self.author = author
        self.info = info
        self.fandom = fandom
        self.url = url
        self.description = description
        self.chapters = chapters
        self.chapters = chapters
