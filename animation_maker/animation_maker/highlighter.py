from variable import *
import copy

def highlight(to_change_variable):
    highlighted = copy.deepcopy(to_change_variable)
    print(highlighted.color)
    highlighted.color = color(0,0,255)
    print(highlighted.color)
    return highlighted
