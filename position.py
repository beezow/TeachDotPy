class Point:
    x = 0
    y = 0
    def __init__(self, a, b):
        self.x = a
        self.y = b

def get_x_on_center(r, c):
    return (r - 1) / 2

def get_y_on_center(r, c):
    return (c - 1) / 2

point1 = Point(5,3)
print(point1.x)
