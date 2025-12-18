class MyPoint:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):  # greather than
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return MyPoint(self.x + other.x, self.y + other.y)
