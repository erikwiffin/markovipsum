from basehash import base62
import random

from domain.model import blog, generated
from infrastructure.mapping.sql import Session

class PostRepository(blog.PostRepository):

    def __init__(self):
        self.__session = Session()

    def add(self, post):
        self.__session.add(post)

    def commit(self):
        self.__session.commit()

    def range(self, limit, offset=0):
        query = self.__session.query(blog.Post)
        return query.limit(limit).offset(offset).all()

class IpsumRepository(generated.IpsumRepository):

    def __init__(self):
        self.__session = Session()

    def hash(self):
        return base62().hash(random.randint(0, 62 ^ 5), 5)

    def oneOfHash(self, hash):
        query = self.__session.query(generated.Ipsum)
        return query.filter(generated.Ipsum.hash == hash).one()

    def add(self, ipsum):
        self.__session.add(ipsum)

    def commit(self):
        self.__session.commit()
