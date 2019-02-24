import json
import copy
from variable import *
from frame import *
from visual_list import *
from json_parser import *
from two_dimensional_list import *

w = 1080
h = w * 2 / 3

var = None
slides = []
slide_number = 0
def setup():
    global var, slides, slide_number
    size(w, h)

    object_tracker = []
    
    another_list = list_of_objects("../../test/ld_array_modification.json")
    for p in another_list:
        if p in object_tracker:
            replaceIndex = object_tracker.index(p)
            object_tracker[replaceIndex] = p
        else:
            object_tracker.append(p)
        slides.append(Frame(copy.deepcopy(object_tracker)))
        
    # var = Variable('i', '1', 255, 255)
    # object_tracker.append(var)
    # newFrame = Frame(copy.deepcopy(object_tracker))
    # slides.append(newFrame)
        
    # var2 = Variable('j', '2', 360, 360)
    # object_tracker.append(var2)
    # slides.append(Frame(copy.deepcopy(object_tracker)))
    
    # vis_list = Visual_List('list', [1,2,3,4], 30, 30)
    # object_tracker.append(vis_list)
    # slides.append(Frame(copy.deepcopy(object_tracker)))
    
    # two_d = Two_Dimensional_List('2Dlist', [[1,2,3,4,5],[3,4],[5,6]], 30, 30)
    # object_tracker.append(two_d)
    # slides.append(Frame(copy.deepcopy(object_tracker)))
    
def draw():
    background(255)
    if (len(slides) != 0): 
        slides[slide_number].draw()
    else:
        print("JSON FILE IS EMPTY")
    
def keyReleased():
    global slide_number
    if (key == CODED):
        if keyCode == RIGHT and (slide_number + 1 < len(slides)):
            slide_number += 1

        if keyCode == LEFT and (slide_number - 1 >= 0):
            slide_number -= 1
