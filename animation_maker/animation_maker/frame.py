class Frame(object):
    def __init__(self, objects):
        self.objects = objects
        
    def draw(self):
        for object in self.objects:
            object.draw(color(255, 255, 255))
