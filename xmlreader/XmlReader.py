from xml.etree import ElementTree
from datetime import datetime
from typing import Any
from os import path
import re


class XmlReader:
    def __init__(self):
        self.types = {}
        self.datetime_format = None

    def register(self, ctor: Any):
        temp = ctor()
        self.types[type(temp).__name__] = (ctor, temp.__dict__.keys())

    def set_datetime_format(self, format: str):
        if format is not None and len(format) > 0:
            self.datetime_format = format

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
                if isinstance(current_object.__dict__[tag], list):
                    current_object.__dict__[tag].append(value)
                else:
                    converted_value = self.__convert(current_object.__dict__[tag], value)
                    current_object.__dict__[tag] = converted_value

    def __convert(self, current, new):
        if current is None or isinstance(current, str):
            return new
        if isinstance(current, int):
            return int(new)
        if isinstance(current, float):
            return float(new)
        if isinstance(current, datetime) and self.datetime_format is not None:
            return datetime.strptime(new, self.datetime_format)




