from visual_list import *

class Queue_List(Visual_List):
    
    def push(self, val):
        self.data.append(val)
    
    def pop(self):
        if (self.data > 0):
            self.data.remove(0)
