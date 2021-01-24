class Person:
    """A person class with
    a name and an age attributes

    """

    def __init__(self, name, age):
        """Initializes the
        Args:
            name - name of the person
            age - the person's age

        """
        self.name = name
        self.age = age

    def say_hi(self):
        """A method that allows the person
        to say hi.

        """
        print("Hi,", self.name)

    def my_age(self):
        """Print the combination the persons's
        name and age respectively

        """
        print(self.name + " is ", self.age)


p = Person("Musa", 10)
p.say_hi()
p.my_age()
