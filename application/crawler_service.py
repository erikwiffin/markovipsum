import datetime

from infrastructure.persistence import http, sql

class CrawlerService(object):
    """crawls websites
    """

    blogs = [
            ("Carpe Durham", 250),
            #("Carpe Durham Wordpress", 250),
            ("Triangle Explorer", 250),
            ("Triangle Food Blog", 50),
            ]

    def scrape(self):

        other_repo = sql.PostRepository()

        for name, count in self.blogs:

            repo = http.PostRepository.factory(name)
            posts = repo.range(count)

            for key, post in enumerate(posts):
                other_repo.add(post)
                if (key % 50 == 0):
                    other_repo.commit()

            other_repo.commit()
