import datetime

from infrastructure.persistence import http
from infrastructure.persistence import sql
from domain.model import blog

class CrawlerService(object):
    "crawls websites"

    def test(self):
        repo = http.PostRepository.factory('Carpe Durham')
        date = datetime.datetime(2008, 1, 1)
        posts = repo.manyUntil(date)

        other_repo = sql.PostRepository()
        for post in posts:
            other_repo.add(post)
        other_repo.commit()
