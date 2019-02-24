import json
import ast
import copy
import re
from visual_list import *
from variable import *
from highlighter import *

def list_of_objects(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        objects = []
        for p in data["steps"]:
            if p["type"] == "<collections.deque>":
                objects.append(Visual_List(p["name"], p["type"], p["data"], p["index"], size = width / 12))
            if p["type"] == "<class 'list'>":
                objects.append(Visual_List(p["name"], p["data"], 0, 0, size = width / 12))
            if p["type"] == "<class 'int'>":
                if check_array_access(p["name"]):
                    list_name_stripped = p["name"].split('[')[0]
                    index_name = re.findall("(?<=\[)[^\]+]", p["name"])
                    
                    to_modify = get_item(objects, list_name_stripped)
                    index_var = get_item(objects, index_name)
                    #print(index_name)
                    #print(to_modify.data)
                    
                    copied_array = copy.deepcopy(to_modify.data)
                    copied_array[index_var.data] = p["data"]
                    
                    vis_list = Visual_List(list_name_stripped, copied_array, 0, 0)
                    
                    vis_list.var_collection[index_var.data] = highlight(vis_list.var_collection[index_var.data])

<<<<<<< HEAD
                    objects.append(Visual_List(list_name_stripped, copied_array, 0, 0, size = width / 12))
=======
                    objects.append(vis_list)
>>>>>>> 103497c89f510b7fbc6b7608d490a104fd7ecf14
                    #print(copied_array)
                else:
                    objects.append(Variable(p["name"], p["data"], 100, (3 * width / 32) * p["data"]), size = width / 12)
            if p["type"] == "<class 'string'>":
                objects.append(Variable(p["name"], p["data"], 100, 100))
        return objects
    
def check_array_access(string):
    ind = re.findall("(?<=\\w)\[.+\]$", string)
    if len(ind) == 0:
        return False
    else:
        indices = ind[0]
        return len(re.findall("\[\]", indices)) == 0
    
def get_item(objects, name):
    '''
    Takes a list of objects and returns one with the correct name
    '''
    for i in range(len(objects) - 1, -1, -1):
        if isinstance(name, list):
            name = name[0]
        if objects[i].name == name:
            return objects[i]
    return None
