class Employee:
	def emaplyoyees_details(self):
		self.name = "Musa"
		self.age = 20
		print("Name is: {} ".format(self.name))
		print("Age is: {} ".format(self.age))

	@staticmethod
	def print_employees_details():
		print("age")

employee = Employee()
employee.emaplyoyees_details()
employee.print_employees_details()