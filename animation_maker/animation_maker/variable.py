class Variable(object):
    def __init__(self, name, data, x, y, size=40):
        self.name = name
        self.data = data
        self.x = x
        self.y = y
        self.size = size

    def draw(self, color):
        TEXTSIZE = 18
        fill(color)
        rect(self.x, self.y, self.size, self.size)
        fill(0)
        text(str(self.data), self.x + TEXTSIZE, self.y + TEXTSIZE)
        textSize(18)
        text(self.name, self.x, self.y + self.size + TEXTSIZE)

    def update_data(self, data):
        self.data = data
