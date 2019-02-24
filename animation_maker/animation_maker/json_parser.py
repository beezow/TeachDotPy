import json
import ast
import copy
import re
from visual_list import *
from queue_list import *
from variable import *
from highlighter import *
from two_dimensional_list import *

def list_of_objects(file_name):
    top_margin = width / 72
    with open(file_name) as json_file:
        data = json.load(json_file)
        objects = []
        for p in data["steps"]:
            if p["type"] == "<class 'queue.Queue'>":
                objects.append(Queue_List(p["name"], p["data"], y=top_margin, size = width / 12))
            elif p["type"] == "<class 'queue.Queue'>-put":
                copied_queue = copy.deepcopy(get_item(objects, p["name"]))
                # Highlighting done in queue
                copied_queue.put(p["data"])
                objects.append(copied_queue)
            elif p["type"] == "<class 'queue.Queue'>-get":
                copied_queue = copy.deepcopy(get_item(objects, p["name"]))
                copied_queue.get()
                copied_queue.y += copied_queue.block_width + copied_queue.gap * 2 + 1
                copied_queue.update_var_collection()
                print(copied_queue.y)
                print("Queue get")
                objects.append(copied_queue)

            if p["type"] == "<class 'list'>":
                if len(p["data"]) != 0 and isinstance(p["data"][0], list):
                    # 2d array
                    new_2d_list = Two_Dimensional_List(p["name"], p["data"], y=top_margin, size = width / 12)
                    objects.append(new_2d_list)
                    #print("it's a list")
                else:
                    # 1d array
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
                    objects.append(Variable(p["name"], p["data"], 100, top_margin, size = width / 12))
            if p["type"] == "<class 'list'>-acc":
                to_modify = get_item(objects, p["name"])
                if len(p["index"]) == 2:
                    index = p["index"]
                    copy_data = copy.deepcopy(to_modify.data)
                    
                    two_list = Two_Dimensional_List(p["name"], copy_data, y = top_margin)
                    
                    two_list.highlight_coord(index[1], index[0])
                    #two_list.var_collection[0].color = color(0, 0, 255)
                    #two_list.var_collection[y * len_x + x] = highlight(two_list.var_collection[y * len_x + x])
                    objects.append(two_list)
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
