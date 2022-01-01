class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hi,", self.name)

    def my_age(self):
        print(self.name + " is ", self.age)


p = Person("Musa", 10)
p.say_hi()
p.my_age()
