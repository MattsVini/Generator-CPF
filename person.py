class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self):
        self.name = input("What is your name? ")
    def set_age(self):
        self.age = int(input("What is age old?"))
    def get_name(self):
        name = self.name
        return name.upper()

    def get_age(self):
        age = self.age
        return age