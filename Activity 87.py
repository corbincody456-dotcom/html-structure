class Point:
    def __init__(self, X=0, Y=0):
        self.x = X
        self.y = Y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

p1 = Point(2, 3)
print(p1)