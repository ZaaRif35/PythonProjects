class MyPet():
    name = 'bublik'
    age = 3

dog = MyPet()

print(dog.name)
print(dog.age)

p1 = Person("ZaaRif", 18)

print(p1.name)
print(p1.age)

class MyPet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Mp = MyPet("Bublik", 3)

print(Mp.name)
print(Mp.age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hi my name is ", self.name)

    def say_bye(self):
        print("Bye " + self.name)
        self.say_hi()

    def say_age(self):
        print("My age is ", self.age)


p1 = Person("ZaaRif", 18)
p1.say_age()