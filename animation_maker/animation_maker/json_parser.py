import json
import ast
from visual_list import *
from variable import *

class Queue:
    def __init__(self, name, type, data, index):
        self.name = name
        self.type = type
        self.data = data
        self.index = index

class Int:
    def __init__(self, name, type, data, index):
        self.name = name
        self.type = type
        self.data = data
        self.index = index

class String:
    def __init__(self, name, type, data, index):
        self.name = name
        self.type = type
        self.data = data
        self.index = index

class List:
    def __init__(self, name, type, data, index):
        self.name = name
        self.type = type
        self.data = data
        self.index = index

def list_of_objects(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        objects = []
        for p in data["steps"]:
            if p["type"] == "<collections.deque>":
                objects.append(Visual_List(p["name"], p["type"], p["data"], p["index"], 0, 0))
            if p["type"] == "<class 'list'>":
                objects.append(Visual_List(p["name"], p["data"], 0, 0))
            if p["type"] == "<class 'int'>":
                objects.append(Variable('', p["data"], 0, 45 * p["data"]))
            if p["type"] == "<class 'string'>":
                objects.append(Variable(p["name"], p["data"], 100, 100))
        return objects
