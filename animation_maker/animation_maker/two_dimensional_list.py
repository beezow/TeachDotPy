from variable import *
from visual_list import *

class Two_Dimensional_List(object):
    
    def __init__(self, name, data, x=0, y=0, color = color(255, 255, 255), size = 40, gap = 5):
        self.name = name
        self.data = data
        self.x = x
        self.y = y
        self.size = size
        self.block_width = (size + gap) * len(data) + gap * 3
        self.gap = gap
        
        self.var_collection = []
        self.update_var_collections()
    
    def draw(self):
        myFont = createFont("Monospaced.bold", width / 15)
        textFont(myFont, width / 15)
        textSize(width / 15)

        for var in self.var_collection:
            var.draw()
    
    def set_x(self, x):
        self.x = x
        self.update_var_collections()

    def update_list(self, new_data):
        self.data = new_data
        
    def update_var_collections(self):
        self.var_collection = []
        for i in range(len(self.data)):
            for j, item in enumerate(self.data[i]):
                var_name = ''
                if i == 0 and j == len(self.data[i]) - 1:
                    var_name = self.name
                self.var_collection.append(Variable(var_name, item, self.x + (3 * width / 32) * i, self.y + (3 * width / 32) * j, size = self.size))
