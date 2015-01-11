import datetime

from infrastructure.persistence import sql
from domain.model import blog, markov, city, generated

class IpsumService(object):
    """Generates, stores, and retrieves Markov Ipsum text
    """

    table = None

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
        repo = sql.IpsumRepository()

        text = self.table.get_text(100)
        ipsum = generated.Ipsum(repo.hash(), text)
        repo.add(ipsum)
        repo.commit()

        return ipsum

    def get_ipsum(self, hash):
        repo = sql.IpsumRepository()
        ipsum = repo.oneOfHash(hash)

        return ipsum
