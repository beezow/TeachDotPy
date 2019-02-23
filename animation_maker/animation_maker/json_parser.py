import json

class Stack:
    def __init__(self, name, type, data):
        self.name = name
        self.type = type
        self.data = data

class Int:
    def __init__(self, name, type, data):
        self.name = name
        self.type = type
        self.data = data

class List:
    def __init__(self, name, type, data):
        self.name = name
        self.type = type
        self.data = data

with open('test.json') as json_file:
    data = json.load(json_file)
    objects = []
    for p in data["steps"]:
        if p["type"] == "stack":
            objects.append(Stack(p["name"], p["type"], p["data"]))
        if p["type"] == "list":
            objects.append(List(p["name"], p["type"], p["data"]))
        if p["type"] == "int":
            objects.append(Int(p["name"], p["type"], p["data"]))
    for q in objects:
        print(q.data)
