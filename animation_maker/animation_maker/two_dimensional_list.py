from variable import *
from visual_list import *

class Two_Dimensional_List(object):
    def __init__(self, name, data, x, y, color = color(255, 255, 255), size = 40, gap = 5):
        self.name = name
        self.data = data
        self.x = x
        self.y = y

        self.size = size
        self.gap = gap
    
    def draw(self):
        for i in range(self.data):
            Visual_List('list', self.data[i], self.x, self.ys).draw()
            translate(i * 20, 0)
    
    def update_list(self, new_data):
        self.data = new_data
