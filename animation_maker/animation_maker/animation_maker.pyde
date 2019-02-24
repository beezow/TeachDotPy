import json
import copy
from variable import *
from frame import *
from visual_list import *
from json_parser import *

var = None
slides = []
slide_number = 0
def setup():
    global var, slides, slide_number
    size(720, 480)

    object_tracker = []
    
    var = Variable('i', '1', 255, 255)
    object_tracker.append(var)
    newFrame = Frame(copy.deepcopy(object_tracker))
    slides.append(newFrame)
    
    another_list = list_of_objects("test1DList.json")
    for p in another_list:
        p.fill(204)
        object_tracker.append(p)
        slides.append(Frame(copy.deepcopy(object_tracker)))
    
def draw():
    background(255)
    slides[slide_number].draw()
    
def keyReleased():
    global slide_number
    if (key == CODED):
        if keyCode == RIGHT and (slide_number + 1 < len(slides)):
            slide_number += 1
            print(slide_number)

        if keyCode == LEFT and (slide_number - 1 >= 0):
            slide_number -= 1
            print(slide_number)
