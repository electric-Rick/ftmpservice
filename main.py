from lib import carros
from lib import tanques




def main_application():
	f = Carro("manual", "goodyear", "v2", "cherry", 1, "desligado")
	g = tanques.m101.Tanque("1.5mm")
	print(f.status())
	pass


main_application()
