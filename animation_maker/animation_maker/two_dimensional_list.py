from variable import *
from visual_list import *

class Two_Dimensional_List(object):
    
    def __init__(self, name, data, x=0, y=0, color = color(255, 255, 255), size = 40, gap = 5):
        self.name = name
        self.data = data
        self.x = x
        self.y = y
        self.size = size
        self.block_width = size
        self.gap = gap
    
    def draw(self):
        myFont = createFont("Monospaced.bold", width / 15)
        textFont(myFont, width / 15)
        textSize(width / 15)
        for i in range(len(self.data)):
            for j, item in enumerate(self.data[i]):
                var_name = ''
                if i == 0 and j == len(self.data[i]) - 1:
                    var_name = self.name
                Variable(var_name, item, self.x, self.y + (3 * width / 32) * j, size = self.size).draw()
            translate(3 * width / 32, 0)
    
    def set_x(self, x):
        self.x = x

    def update_list(self, new_data):
        self.data = new_data
