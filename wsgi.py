#!/usr/bin/env python

from flask import Flask
from ui import app
from ui.controllers import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
