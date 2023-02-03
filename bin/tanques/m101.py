
class Tanque:
	def __init__(self, blindagem):
		self.b = blindagem
		pass
	def status(self):
		info = self.b
		print(info)
		pass


x = Tanque("1.5mm")
x.status()
