from variable import *
class Frame(object):
    def __init__(self, objects, spacing=15):
        self.objects = objects
        self.spacing = spacing
        
        new_obj_x_coord = self.spacing
        new_obj_y_coord = self.spacing
        for i, object in enumerate(self.objects):
            if isinstance(object, Variable):
                object.y = new_obj_y_coord
                object.x = new_obj_x_coord
                new_obj_y_coord += object.block_height + self.spacing + object.textsize
            else:
                new_obj_y_coord = self.spacing
                
                object.set_x(new_obj_x_coord)
                new_obj_x_coord += object.block_width + self.spacing
        
    def draw(self):
        for object in self.objects:
            object.draw()
