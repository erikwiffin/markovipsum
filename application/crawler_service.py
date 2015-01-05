import datetime

from infrastructure.persistence import http, sql
from domain.model import blog, markov, city

class CrawlerService(object):
    "crawls websites"

    table = None
    blogs = [
            ("Carpe Durham", 250),
            #("Carpe Durham Wordpress", 250),
            #("Triangle Explorer", 250),
            #("Triangle Food Blog", 50),
            ]

    def scrape(self):

        other_repo = sql.PostRepository()

        for name, count in self.blogs:

            repo = http.PostRepository.factory(name)
            posts = repo.range(count)

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

        self.table = table

    def get_text(self):
        return self.table.get_text(100)

#service = CrawlerService()
#service.build()
