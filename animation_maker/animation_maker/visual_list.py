from variable import *

class Visual_List(object):
    color_red = 0
    color_blue = 0
    color_green = 255
    
    def __init__(self, name, data, x, y, color=color(255,255,255), size=40, gap=5):
        self.color_red = Visual_List.color_red
        self.color_green = Visual_List.color_green
        self.color_blue = Visual_List.color_blue
        Visual_List.color_red += 100
        Visual_List.color_blue += 100
        Visual_List.color_green -= 100
        self.name = name
        self.data = data
        self.block_width = size
        self.x = x
        self.y = y

        self.size = size
        self.gap = gap
        
        self.var_collection = []
        self.update_var_collection()
        
    def draw(self):
        stroke(self.color_red,self.color_green, self.color_blue)
        for var in self.var_collection:
            var.draw()
        stroke(0)
            
    def __eq__(self, other):
        '''
        Overrides equality to check only for name equality
        '''
        return self.name == other.name
    
    def update_list(self, new_data):
        self.data = new_data
    
    def set_x(self, x):
        self.x = x
        for var in self.var_collection:
            var.x = x
    
    def update_var_collection(self):
        self.var_collection = []
        for i, item in enumerate(self.data):
            var_name = ''
            if i == len(self.data) - 1:
                var_name = self.name
            #print(self.name, self.x)
            var = Variable(var_name, item, self.x, self.y + (3 * width / 32) * i, size = width / 12)
            self.var_collection.append(var)
