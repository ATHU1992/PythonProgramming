class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, My name is {self.name}")


person = Person("Atharva")
print(person.name)
person.name = "Ameya"
print(person.name)

person.talk()
