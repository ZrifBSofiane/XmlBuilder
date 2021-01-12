from typing import Any
import re
from os import path
from xml.etree import ElementTree


class XmlReader:
    def __init__(self):
        self.types = {}

    def register(self, ctor: Any):
        temp = ctor()
        self.types[type(temp).__name__] = (ctor, temp.__dict__.keys())

    def read(self, file):
        if not path.exists(file):
            return Exception("File not found %s" % file)

        tree = ElementTree.parse(file)
        root = tree.getroot()
        return self.parse_xml(root, None)

    def parse_xml(self, element, current_obj):
        if not element.getchildren():
            tag = re.sub('{.*}', '', element.tag)
            key = type(current_obj).__name__
            self.__affect_value(key, tag, current_obj, element.text)
        else:
            if element.tag in self.types:
                parent = self.types[element.tag][0]()
            else:
                return current_obj
            for elem in element.getchildren():
                current_obj = self.parse_xml(elem, parent)
                key = type(parent).__name__
                tag = type(current_obj).__name__
                self.__affect_value(key, tag, parent, current_obj)
        return current_obj

    def __affect_value(self, key, tag, current_object, value):
        if key in self.types:
            if tag in self.types[key][1]:
                current_object.__dict__[tag] = value



