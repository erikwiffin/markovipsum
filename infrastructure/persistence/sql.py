from domain.model import blog
from infrastructure.mapping.sql import Session

class PostRepository(blog.PostRepository):

    def __init__(self):
        self.__session = Session()

    def add(self, post):
        self.__session.add(post)

    def commit(self):
        self.__session.commit()

    def manyUntil(self, post):
        pass
