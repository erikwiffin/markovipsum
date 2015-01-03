from .. import manager
from application.crawler_service import CrawlerService

@manager.command
def test():
    "I'm just a test"
    service = CrawlerService()
    service.test()
