'''
This file is used to draw physical shapes using processing.py
'''
def setup():
    size(1000, 500)
    
def draw():
    background(255)
    #create_rectangle(0,0,55,55)
    #color_rectangle(100, 100, 100, 100, 150, 0, 0)
    create_arrow(1000, 200, 200, 'left')

'''
x and y are the center coordinates for shapes.
'''

def create_arrow(size, x, y, direction):
    strokeWeight(4)
    if direction == 'left' or direction == 'right':
        line(x - size / 2, y, x + size / 2, y)
        if direction is 'left':
            triangle(x - size / 2, y - 20, x - size / 2, y + 20, x - size / 2 - 20, y)
        else:
            triangle(x + size / 2, y - 20, x + size / 2, y + 20, x + size / 2 + 20, y)

    elif direction == 'up' or direction == 'down':
        line(x, y - size / 2, x, y + size / 2)
        if direction == 'up':
            triangle(x - 20, y - size / 2, x + 20, y - size / 2, x, y - size / 2 - 20)
        else:
            triangle(x - 20, y + size / 2, x + 20, y + size / 2, x, y + size / 2 - 20)
    
    
    
