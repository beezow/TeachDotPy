import json
from variable import *
var = None
def setup():
    global var
    size(720, 480)
    with open('test.json') as f:
        data = json.load(f)
        print(data)
    
    var = Variable('counter', '1', 255, 255)
    
def draw():
    background(255)
    var.draw(color(44, 218, 240))
