class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<{self.x}, {self.y}>"



a = Coordinate(1,2)
print(a)