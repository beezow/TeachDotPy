import json
import ast

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
                objects.append(Queue(p["name"], p["type"], p["data"], p["index"]))
            if p["type"] == "<class 'list'>":
                objects.append(List(p["name"], p["type"], p["data"], p["index"]))
            if p["type"] == "<class 'int'>":
                objects.append(Int(p["name"], p["type"], p["data"], p["index"]))
            if p["type"] == "<class 'string'>":
                objects.append(String(p["name"], p["type"], p["data"], p["index"]))
        return objects

list_of_objects("test1DList.json")
