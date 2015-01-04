import random, re

class Markov(object):
    """This class holds a Markov table

    _lookahead
    _table
    _bonus_words
    """

    def __init__(self, lookahead=3):
        self._lookahead = lookahead
        self._table = {}
        self._bonus_words = []

    def set_bonus_words(self, text):
        words = re.split(r"\s+", text, flags=re.UNICODE)
        self._bonus_words = set(words)

    def add_text(self, text):
        words = re.split(r"\s+", text, flags=re.UNICODE)

        key = (None,)*self._lookahead

        for word in words:
            self._table.setdefault( key, [] ).append(word)
            if word in self._bonus_words:
                self._table[key].append(word)
            key = advance(key, word)

    def get_text(self, words):
        text = ''

        key = (None,)*self._lookahead

        for i in xrange(words):
            newword = self.__next_word(key)
            text += ' ' + newword
            key = advance(key, newword)

        return text

    def __next_word(self, key):
        return random.choice(self._table.get(key, ['']))

def advance(key, word):
    key = list(key)
    del key[0]
    key.append(word)

    return tuple(key)
