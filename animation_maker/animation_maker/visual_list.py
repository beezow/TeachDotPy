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
    
    def draw(self):
        stroke(self.color_red,self.color_green, self.color_blue)
        for i, item in enumerate(self.data):
            var_name = ''
            if i == len(self.data) - 1:
                var_name = self.name
            Variable(var_name, item, self.x, self.y + (3 * width / 32) * i).draw()
        stroke(0)
            
    def __eq__(self, other):
        '''
        Overrides equality to check only for name equality
        '''
        return self.name == other.name
    
    def update_list(self, new_data):
        self.data = new_data
