"""Overriding:
To redefine the base class method within your derived class

 Method resolution order

"""


class Employee:

    def set_working_hour(self):
        self.num_of_work_hour = 30

    def display_working(self):
        print(self.num_of_work_hour)


class Trainee(Employee):
    def set_working_hour(self):
        """Override the number of working hours"""
        self.num_of_work_hour = 50

    def reset_working(self):
        """Reset number of working as indicated in the based class"""
        super().set_working_hour()


employee = Employee()
employee.set_working_hour()
print("Number of working hours of employees before reset ", end=' ')
employee.display_working()

trainee = Trainee()
trainee.set_working_hour()
print("Number of working hours of trainees are ", end=' ')
trainee.display_working()

# Reset num of working hour
trainee.reset_working()
print("Number of working hours of trainees after reset ", end=' ')
trainee.display_working()
