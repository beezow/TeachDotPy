from visual_list import *
from highlighter import *

class Queue_List(Visual_List):
    
    def put(self, val):
        self.data.append(val)
        self.update_var_collection()
        self.var_collection[-1] = highlight(self.var_collection[len(self.var_collection) - 1])
    
    def get(self):
        if (self.data > 0):
            del self.data [0]
            self.update_var_collection()
            
