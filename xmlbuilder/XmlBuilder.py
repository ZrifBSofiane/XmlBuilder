from typing import Any
import re
from os import path
from xml.etree import ElementTree


class XmlBuilder():

    def __init__(self):
        self.types = {}

    def register(self, ctor: Any):
        temp = ctor()
        self.types[type(temp).__name__] = (ctor, temp.__dict__.keys())

    def read(self, file):
        if not path.exists(file):
            print("File doesnt exists")

        tree = ElementTree.parse(file)
        root = tree.getroot()
        a = self.lxml_to_dict(root)
        return a

    def lxml_to_dict(self, element):
        ret = {}
        result = None
        if element.getchildren() == []:
            tag = re.sub('{.*}', '', element.tag)
            ret[tag] = element.text
            result = element.text
        else:
            print("Its a list " + element.tag)
            result = self.types[element.tag][0]()
            count = {}
            for elem in element.getchildren():
                subdict = self.lxml_to_dict(elem)
                result.__dict__[elem.tag] = subdict
        return result


