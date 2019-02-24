class Frame(object):
    def __init__(self, objects, spacing=15):
        self.objects = objects
        self.spacing = spacing
        
    def draw(self):
        new_obj_x_coord = self.spacing
        #print(type(self.objects[0]))
        for i, object in enumerate(self.objects):
            object.x = new_obj_x_coord
            object.draw()
            new_obj_x_coord += object.block_width + self.spacing
