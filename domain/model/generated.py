from abc import ABCMeta, abstractmethod

class IpsumRepository(object):
    """A Repository of Generated Blocks of Text
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def oneOfHash(self, hash):
        """Return a single Ipsum identified by a hash
        """
        pass

    @abstractmethod
    def add(self, ipsum):
        """Add a single Ipsum to the Repository
        """
        pass

    @abstractmethod
    def commit(self):
        """Commit added Ipsums to the persistence mechanism
        """
        pass


class Ipsum(object):

    def __init__(self, hash, text):
        self.hash = hash
        self.text = text
