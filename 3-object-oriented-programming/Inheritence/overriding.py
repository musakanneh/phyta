class Employee:

    def set_working_hour(self):
        self.num_of_work_hour = 30

    def display_working(self):
        print(self.num_of_work_hour)


class Trainee(Employee):
    def set_working_hour(self):
        self.num_of_work_hour = 50

    def reset_working(self):
        super().set_working_hour()


employee = Employee()
employee.set_working_hour()
print("Number of working hours of employees before reset ", end=' ')
employee.display_working()

trainee = Trainee()
trainee.set_working_hour()
print("Number of working hours of trainees are ", end=' ')
trainee.display_working()

trainee.reset_working()
print("Number of working hours of trainees after reset ", end=' ')
trainee.display_working()
