class Mammals:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")


class Dog(Mammals):
    pass


class Cat(Mammals):
    pass


cat1 = Cat("Kyle")
cat1.walk()

dog1 = Dog("Rocky")
dog1.walk()