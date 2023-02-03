class Carro:
	def __init__(self, direcao, rodas, motor, modelo,chave, estado):
		self.d = direcao
		self.r = rodas
		self.m = motor
		self._m = modelo
		self.k  = chave
		self.e = estado
		pass

	def status(self):
		print(self.d, self.r, self.m, self._m)
		pass
	def ligar(self):
		if self.k == 0:
			print("Você precisa de uma chave para ligar o carro")
		else:
			self.e = "ligado"
			print("Carro ligado...")
		pass

	def andar(self, posicao):
		if self.e == "ligado":
			for x in range(10):
				x = x+1
				y = x+1
				posicao['x'] = x
				posicao['y'] = y
				print("Metros andados[x]:", x, "m")
				print("Metros andados[y]:", y, "m")
		else:
			print("Não posso andar, estou desligado")
			pass


