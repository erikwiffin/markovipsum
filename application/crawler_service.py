import datetime

from infrastructure.persistence import http, sql
from domain.model import blog, markov, city

class CrawlerService(object):
    "crawls websites"

    blogs = [
            "Carpe Durham",
            "Triangle Explorer",
            "Triangle Food Blog"]

    def scrape(self):

        other_repo = sql.PostRepository()

        for name in self.blogs:

            repo = http.PostRepository.factory(name)
            posts = repo.range(250)

            for key, post in enumerate(posts):
                other_repo.add(post)
                if (key % 100 == 0):
                    other_repo.commit()

            other_repo.commit()

    def build(self):
        repo = sql.PostRepository()
        posts = repo.range(10000)

        table = markov.Markov(2)
        table.set_bonus_words(city.durham)

        for post in posts:
            table.add_text(post.title)
            table.add_text(post.body)

        return table.get_text(100)
