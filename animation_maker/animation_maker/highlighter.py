from variable import *
import copy

def highlight(to_change_variable):
    highlighted = copy.deepcopy(to_change_variable)
    highlighted.color = color(255,255,51)
    return highlighted
