import logging

from . import parser_strategy as ps
from domain.model import blog

class PostRepository(blog.PostRepository):

    __parser_strategy = None

    @staticmethod
    def factory(name):
        if name == "Carpe Durham":
            return PostRepository(ps.CarpeDurham())
        if name == "Triangle Explorer":
            return PostRepository(ps.TriangleExplorer())
        if name == "Triangle Food Blog":
            return PostRepository(ps.TriangleFoodBlog())
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

    def range(self, limit, offset=0):
        post = self.__parser_strategy.first()
        logging.info(post)
        i = 0
        while post is not None and i < limit + offset:
            i += 1
            if (i < offset):
                post = self.__parser_strategy.next()
                continue

            yield blog.Post(
                    title=post['title'],
                    body=post['body'],
                    date=post['date'],
                    url=post['url'],
                    city=self.__parser_strategy.city)
            post = self.__parser_strategy.next()
