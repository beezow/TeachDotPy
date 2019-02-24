from variable import *
import copy

def highlight(to_change_variable):
    highlighted = copy.deepcopy(to_change_variable)
    #print(highlighted.color)
    highlighted.color = color(255,255,51)
    #print(highlighted.color)
    return highlighted
