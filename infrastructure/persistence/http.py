import logging
from parser_strategy import CarpeDurham

from domain.model import blog

class PostRepository(blog.PostRepository):

    __parser_strategy = None

    @staticmethod
    def factory(name):
        if name == "Carpe Durham": return PostRepository(CarpeDurham())
        return None

    def __init__(self, parser_strategy):
        self.__parser_strategy = parser_strategy

    def manyUntil(self, date):
        post = self.__parser_strategy.first()
        logging.info(post)
        while post is not None and post['date'] > date:
            yield blog.Post(
                    title=post['title'],
                    body=post['body'],
                    date=post['date'],
                    url=post['url'],
                    city=self.__parser_strategy.city)
            post = self.__parser_strategy.next()
