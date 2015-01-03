#!/usr/bin/env python

from flask import Flask
import logging

from ui import manager
from ui.commands import *

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    manager.run()
