import os
from xmlreader.XmlReader import XmlReader


class prices:
    def __init__(self):
        self.open = None
        self.close = None

    def average(self):
        return (self.open + self.close) * 0.5


class stock:
    def __init__(self):
        self.name = None
        self.isin = None
        self.prices = None


class stocks:
    def __init__(self):
        self.priceDate = None
        self.stock = []


builder = XmlReader()
builder.register(lambda: stocks())
builder.register(lambda: stock())
builder.register(lambda: prices())

current_path = os.curdir
file = os.path.join(current_path, 'Files', 'readXml.xml')

objet = builder.read(file)
a = 5


