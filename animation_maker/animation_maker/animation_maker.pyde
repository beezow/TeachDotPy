import json
import copy
from variable import *
from frame import *
from visual_list import *
from json_parser import *
from two_dimensional_list import *

w = 1080
h = int(w * 2 / 2.8)

var = None
slides = []
slide_number = 0
def setup():
    global var, slides, slide_number
    size(w, h)
    
    
    myFont = createFont("Monospaced.bold", width / 15)
    textFont(myFont, width / 15)
    textSize(width / 15)

    # Accumulates each object to be taken a copy of to the frame object
    object_tracker = []
    
    graphic_objects = list_of_objects("../../test/spiral_matrix.json")
    #graphic_objects = list_of_objects("log/teach.json")
    for graphic in graphic_objects:
        if graphic in object_tracker:
            replaceIndex = object_tracker.index(graphic)
            object_tracker[replaceIndex] = graphic
        else:
            object_tracker.append(graphic)
        slides.append(Frame(copy.deepcopy(object_tracker)))
    
def draw():
    background(255)
    if (len(slides) != 0): 
        slides[slide_number].draw()
    else:
        print("JSON FILE IS EMPTY")
    
def keyReleased():
    global slide_number
    if (key == "q"):
        exit()
    if (key == CODED):
        if keyCode == RIGHT and (slide_number + 1 < len(slides)):
            slide_number += 1

        if keyCode == LEFT and (slide_number - 1 >= 0):
            slide_number -= 1

            
