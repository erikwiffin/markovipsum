from abc import ABCMeta, abstractmethod

class PostRepository(object):
    """A Repository of Blog Posts
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def range(self, limit, offset=0):
        """Return all the Blog Posts inside a given range
        """
        pass

    @abstractmethod
    def add(self, post):
        """Add a single Blog Post to the Repository
        """
        pass

    @abstractmethod
    def commit(self):
        """Commit added Blog Posts to the persistence mechanism
        """
        pass


class Post(object):

    def __init__(self, title, body, date, url, city):
        self.title = title
        self.body = body
        self.date = date
        self.url = url
        self.city = city
