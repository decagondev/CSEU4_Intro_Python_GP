# composition and inheritance

class Bar:
    def __init__(self, name="bar"):
        self.name = name


class Foo:
    def __init__(self):
        self.bar = [Bar()] * 10

    def __str__(self):
        return f"{self.bar}"


foo = Foo()

print(foo)
