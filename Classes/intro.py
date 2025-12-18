class MyPoint:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    @classmethod
    def zer(cls):
        return cls(0, 0)

    def draw(self):
        print("draw")


point = MyPoint(1, 2)
point.default_color
point.z = 10
point.draw()


another = MyPoint(3, 4)
