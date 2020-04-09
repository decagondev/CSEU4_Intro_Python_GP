# composition and inheritance


class Bar:
    def __init__(self, name="bar"):
        self.name = name

a = 12
b = 23
c = 19

class Foo:
    def __init__(self):
        self.bars = [Bar()] * 10 # has_a relationship
        self.numbers = [a, b, c] # has_a

    def __str__(self):
        return f"{self.bar}"


class Entity():
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def get_id(self):
        return self.id


my_super = Entity()


class Mob(Entity): # is_a relationship
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        # self.bob = super().get_id()

foo = Foo()

print(foo)
