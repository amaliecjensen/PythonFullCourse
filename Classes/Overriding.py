class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__
        self.weight = 2

    def walk(self):
        print("walk")


class Fisk(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
m.walk()
m.age()
print(isinstance(m, object))
