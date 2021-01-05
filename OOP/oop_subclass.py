class SchoolMember:
    """Represents any school member.
    Execute the process of inheritance

    """

    def __init__(self, name, age):
        """Initializes the student's details.
        Then, prints out the output

        """
        self.name = name
        self.age = age
        print("Intialized school member: {} ".format(name))

    def tell(self):
        """Prints out the school member details."""
        print("Name{}, and Age: {:d}".format(self.name, self.age), end="")


class Teacher(SchoolMember):
    """Represents the teacher class with artributes
    inherited from the SchoolMember class

    """

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("Initialized Teacher: {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    """Represents a student."""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()
members = [t, s]
for member in members:
    member.tell()
