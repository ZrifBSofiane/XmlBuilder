from datetime import datetime
import os
import unittest

from xmlreader.XmlReader import XmlReader


class TestReadXml(unittest.TestCase):

    def test_should_read_xml_and_parse(self):
        class prices:
            def __init__(self):
                self.open = 0.0
                self.close = 0.0

            def average(self):
                return (self.open + self.close) * 0.5

        class stock:
            def __init__(self):
                self.name = None
                self.isin = None
                self.prices = None

        class stocks:
            def __init__(self):
                self.priceDate = datetime.min
                self.stock = []


        reader = XmlReader()
        reader.set_datetime_format("%Y/%m/%d")
        reader.register(lambda: stocks())
        reader.register(lambda: stock())
        reader.register(lambda: prices())

        current_path = os.curdir
        file = os.path.join(current_path, 'Files', 'readXml.xml')

        result = reader.read(file)
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result.priceDate, datetime))
        self.assertEqual(datetime(2020, 1, 1), result.priceDate)
        self.assertEqual(2, len(result.stock))
        self.assertEqual("Apple", result.stock[0].name)
        self.assertEqual("AAPL", result.stock[0].isin)
        self.assertEqual(127.5, result.stock[0].prices.average())
        self.assertEqual("Tesla", result.stock[1].name)
        self.assertEqual("TSLA", result.stock[1].isin)
        self.assertEqual(155, result.stock[1].prices.average())


