from variable import *
from visual_list import *
from highlighter import *

class Two_Dimensional_List(object):
    
    color_red = 0
    color_blue = 0
    color_green = 255
    
    def __init__(self, name, data, x=0, y=0, color = color(255, 255, 255), size = 90, gap = 5):
        self.color_red = Two_Dimensional_List.color_red
        self.color_green = Two_Dimensional_List.color_green
        self.color_blue = Two_Dimensional_List.color_blue
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
        stroke(self.color_red, self.color_green, self.color_blue)
        for var in self.var_collection:
            var.draw()
            #print(red(var.color), green(var.color), blue(var.color))
        stroke(0)

    def __eq__(self, other):
        '''
        Overrides equality to check only for name equality
        '''
        return self.name == other.name
    
    def highlight_coord(self, x, y):
        len_y = len(self.data)
        len_x = len(self.data[0])
        self.var_collection[y * len_x + x] = highlight(self.var_collection[y * len_x + x])
        #self.var_collection[y * len_x + x].color = 0
    
    def set_x(self, x):
        self.x = x
        index = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.var_collection[index].x = self.x + (3 * width / 32) * i
                index += 1
                #self.var_collection[index].y = self.y + (3 * width / 32) * j,
                
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
