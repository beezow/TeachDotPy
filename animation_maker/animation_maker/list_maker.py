'''
data is the list parameter.
'''
import ast
class List(Object):
    
    canvas_length = 500
    canvas_width = 100
    
    def __init__(self, data):
        self.data = data
    
    def draw(self):
        list self.data
        size = len(list)
        length = canvas_length / size - 10
        width = 100
        object_name = ''
        for i in range(size):
            textSize(32);
            rect(0, CENTER, length, width, length / 5)
            translate(length * i, 0)
            name = str(i)
            text(name, length * i + 10, width / 2);
            textAlign(CENTER, CENTER);
            
    
        #rect(x, y, length, width, 7);
        
    def update_data(self, data):
        self.data = data

    
    
    
