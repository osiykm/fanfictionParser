from datetime import date


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


@_auto_str
class FanficData:
    def __init__(self, name: str = "", author: AuthorData = AuthorData(), description: str = "", size: int = 0,
                 updated: date = date.today(), created: date = date.today(), chapters=[]):
        self.name = name
        self.author = author
        self.size = size
        self.updated = updated
        self.created = created
        self.description = description
        self.chapters = chapters
