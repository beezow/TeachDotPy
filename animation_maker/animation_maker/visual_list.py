from variable import *

class Visual_List(object):
    def __init__(self, name, data, x, y, color=color(255,255,255), size=40, gap=5):
        self.name = name
        self.data = data
        self.x = x
        self.y = y
        
        self.size = size
        self.gap=5
        
        # adding all variable elements 
        self.list_vars = []
        for i, item in enumerate(data):
            var_name = ''
            if i == len(data) - 1:
                var_name = name
            self.list_vars.append(Variable(var_name, item, x, y + i * (size + gap)))
    
    def draw(self):
        for i, var in enumerate(self.list_vars):
            var.set_coords(self.x, self.y + i * (self.size + self.gap))
            var.draw()
            
    # def update_list(self, new_data):
    #     for i, item in enumerate(new_data):
    #         var_name = ''
    #         if i == len(data) - 1:
    #             var_name = name
    #         self.list_vars.append(Variable(var_name, item, x, y + i * (size + gap)))
