from abc import ABCMeta, abstractmethod

class PostRepository(object):
    """A Repository of Blog Posts
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def manyUntil(self, date):
        """Return a list of Blog Posts until a date in the past is reached"""
        pass


class Post(object):

    def __init__(self, title, body, date, url, city):
        self.title = title
        self.body = body
        self.date = date
        self.url = url
        self.city = city
