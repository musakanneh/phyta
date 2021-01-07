class Employee:
	""" """

	count = 0
	def __init__(self, name):
		self.name = name
		

	def display_details(self):
		print("{}".format(self.name))


employee = Employee("Musa Kanneh")
employee.display_details()