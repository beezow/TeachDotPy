import json
import ast
import copy
import re
from visual_list import *
from queue_list import *
from variable import *
from highlighter import *

def list_of_objects(file_name):
    top_margin = width / 72
    with open(file_name) as json_file:
        data = json.load(json_file)
        objects = []
        for p in data["steps"]:
            if p["type"] == "<class 'queue.Queue'>":
                objects.append(Queue_List(p["name"], p["data"], size = width / 12))
            elif p["type"] == "<class 'queue.Queue'>-put":
                copied_queue = copy.deepcopy(get_item(objects, p["name"]))
                # Highlighting done in queue
                copied_queue.put(p["data"])
                objects.append(copied_queue)
            elif p["type"] == "<class 'queue.Queue'>-get":
                copied_queue = copy.deepcopy(get_item(objects, p["name"]))
                copied_queue.get()
                objects.append(copied_queue)

            if p["type"] == "<class 'list'>":
                new_list = Visual_List(p["name"], p["data"], 0, top_margin, size = width / 12)
                if p["index"] is not None:
                    # need to highlight something
                    new_list.var_collection[-1] = highlight(new_list.var_collection[-1])
                objects.append(new_list)
            if p["type"] == "<class 'int'>":
                if check_array_access(p["name"]):
                    # Checks for a[i] type variables
                    list_name_stripped = p["name"].split('[')[0]
                    index_name = re.findall("(?<=\[)[^\]+]", p["name"])

                    to_modify = get_item(objects, list_name_stripped)
                    index_var = get_item(objects, index_name)
                    
                    copied_array = copy.deepcopy(to_modify.data)
                    copied_array[index_var.data] = p["data"]
                    
                    vis_list = Visual_List(list_name_stripped, copied_array, 0, top_margin, size = width / 12)
                    
                    vis_list.var_collection[index_var.data] = highlight(vis_list.var_collection[index_var.data])

                    objects.append(vis_list)
                else:
                    objects.append(Variable(p["name"], p["data"], 100, top_margin + (3 * width / 32) * p["data"], size = width / 12))
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

def two_dimensional_array(two_dimensional):
    returnArray = []
    for i in two_dimensional["data"]:
        row = []
        for j in i:
            row.append(Variable("", j))
        returnArray.append(row)
    return returnArray

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
