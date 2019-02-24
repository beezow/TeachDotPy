class Variable(object):
    def __init__(self, name, data, x, y, color=color(255,255,255), size=40, textsize=18, spacing=4):
        # var name
        self.name = name
        # data assigned
        self.data = data
        # coordinates
        self.x = x
        self.y = y
        # color of the background cell
        self.color = color
        # standard square size of the cell
        self.size = size
        self.block_width = size
        self.block_height = size
        self.textsize = textsize
        # minimum spacing between text and border of cell
        self.spacing = spacing

    def draw(self):
        fill(self.color)
        # Creates rect with rounded corners
        if textWidth(str(self.data)) > self.size:
            self.block_width = textWidth(str(self.data))
        else:
            self.block_width = self.size
        rect(self.x, self.y, self.block_width, self.block_height, self.size / 5)
        fill(0)
        # Creates data text
        text_x_coord = self.x + (self.block_width - textWidth(str(self.data))) / 2
        text(str(self.data), text_x_coord, self.y + self.textsize)
        textSize(self.textsize)
        
        #Creates variable label text
        text(self.name, self.x, self.y + self.size + self.textsize)
        
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def update_data(self, data):
        self.data = data
        
    '''
    highlights an object
    '''
    
    def re_highlight(self):
        self.highlight = True
        self.tint = color(0, 0, 255)
    
    '''
    Changes a highlighted block back to default
    '''

    def de_highlight(self):
        self.tint = color(255, 255, 255)

    def print_poly(self):
        self.poly.setFill(self.tint)
        self.block = shape(self.poly, self.posx, self.posy)
        textAlign(CENTER)
        textFont(createFont("Arial", self.sizey / 2, True))
        text(self.value, self.posx + int(self.sizex / 2), self.posy + int(self.sizey / 1.5))
