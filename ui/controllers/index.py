from flask import render_template, g, current_app

from application.crawler_service import CrawlerService
from .. import app

service = CrawlerService()
service.build()

@app.route('/')
def index():
    foo = service.get_text()
    return render_template('index.html', foo=foo)
