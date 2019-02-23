class Variable(object):
    def __init__(self, name, data, x, y, color=color(255,255,255), size=40):
        self.name = name
        self.data = data
        self.x = x
        self.y = y
        self.color = color
        self.size = size

    def draw(self):
        TEXTSIZE = 18
        fill(self.color)
        rect(self.x, self.y, self.size, self.size, self.size / 5)
        fill(0)
        text(str(self.data), self.x + TEXTSIZE, self.y + TEXTSIZE)
        textSize(TEXTSIZE)
        
        text(self.name, self.x, self.y + self.size + TEXTSIZE)
        
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def update_data(self, data):
        self.data = data
