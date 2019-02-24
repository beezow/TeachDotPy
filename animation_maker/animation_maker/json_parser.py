import json
import ast
import re
from visual_list import *
from variable import *

def list_of_objects(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        objects = []
        for p in data["steps"]:
            if p["type"] == "<collections.deque>":
                objects.append(Visual_List(p["name"], p["type"], p["data"], p["index"]))
            if p["type"] == "<class 'list'>":
                objects.append(Visual_List(p["name"], p["data"], 0, 0))
            if p["type"] == "<class 'int'>":
                objects.append(Variable(p["name"], p["data"], 100, 45 * p["data"]))
            if p["type"] == "<class 'string'>":
                objects.append(Variable(p["name"], p["data"], 100, 100))
        return objects
