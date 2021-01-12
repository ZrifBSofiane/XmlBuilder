import os
from os import path
from xml.etree import ElementTree
import re

from xmlreader.XmlReader import XmlReader


class note:
    def __init__(self):
        self.to = None
        self.from1 = None
        self.heading = None
        self.body = None


class toDetail:
    def __init__(self):
        self.detail1 = None
        self.detail3 = None


class to:
    def __init__(self):
        self.to1 = None
        self.to2 = None
        self.toDetail = None


builder = XmlReader()
builder.register(lambda: note())
builder.register(lambda: to())
builder.register(lambda: toDetail())

current_path = os.curdir
file = os.path.join(current_path, 'Files', 'readXml.xml')

objet = builder.read(file)
a = 5


