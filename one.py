

print("working one")

class person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __call__(self):
		return "callable"

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

print(callable(person))