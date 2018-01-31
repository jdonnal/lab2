
class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.center = [x+width/2,y+height/2]
        print("building a rect")

    def calcArea(self):
        return self.width*self.height

class Circle:
    def __init__(self):
        print("building a circle")


