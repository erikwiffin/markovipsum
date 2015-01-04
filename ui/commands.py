from application.crawler_service import CrawlerService
from . import manager

@manager.command
def scrape():
    "Scrape a defined list of blogs for words to populate the markov model"
    service = CrawlerService()
    service.scrape()

@manager.command
def build():
    "Build the Markov model from scraped sites"
    service = CrawlerService()
    print service.build()
