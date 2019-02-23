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
    
    def re_highlight(self):
        self.highlight = True
        self.tint = color(0, 0, 255)
    def de_highlight(self):
        self.tint = color(255, 255, 255)

    def print_poly(self):
        self.poly.setFill(self.tint)
        self.block = shape(self.poly, self.posx, self.posy)
        textAlign(CENTER)
        textFont(createFont("Arial", self.sizey / 2, True))
        text(self.value, self.posx + int(self.sizex / 2), self.posy + int(self.sizey / 1.5))
