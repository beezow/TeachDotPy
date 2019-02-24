from variable import *

class Visual_List(object):
    def __init__(self, name, data, x, y, color=color(255,255,255), size=40, gap=5):
        self.name = name
        self.data = data
        self.block_width = size
        self.x = x
        self.y = y

        self.size = size
        self.gap = gap
    
    def draw(self):
        for i, item in enumerate(self.data):
            var_name = ''
            if i == len(self.data) - 1:
                var_name = self.name
            Variable(var_name, item, self.x, self.y + (self.size + self.gap) * i).draw()
            
    def __eq__(self, other):
        '''
        Overrides equality to check only for name equality
        '''
        return self.name == other.name
    
    def update_list(self, new_data):
        self.data = new_data
