from flask import render_template

from application.ipsum_service import IpsumService
from . import app

service = IpsumService()
service.build()

@app.route('/')
def index():
    ipsum = service.get_text()
    return render_template('index.html', ipsum=ipsum)

@app.route('/<hash>')
def hash(hash):
    ipsum = service.get_ipsum(hash)
    return render_template('index.html', ipsum=ipsum)
