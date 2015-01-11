from application.crawler_service import CrawlerService
from . import manager

@manager.command
def scrape():
    "Scrape a defined list of blogs for words to populate the markov model"
    service = CrawlerService()
    service.scrape()
