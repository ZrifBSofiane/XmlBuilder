import os
from os import path
from xml.etree import ElementTree
import re

from xmlbuilder.XmlBuilder import XmlBuilder


class note:

    def __init__(self):
        self.to = None
        self.from1 = None
        self.heading = None
        self.body = None


builder = XmlBuilder()
builder.register(lambda: note())

current_path = os.curdir
file = os.path.join(current_path, 'Files', 'readXml.xml')

objet = builder.read(file)
a = 5


