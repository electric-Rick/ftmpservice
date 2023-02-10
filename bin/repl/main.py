#from input_data import Data
#from gerador_temp.main import Temperatura
import asyncio
import sys
import time
# adicionar modulo que lidará com login do usuário auth_module?
from code import InteractiveConsole

#from db.connection import Connection
class ApplicationReplSession:
	def __init__(self,username,key):
		self.u = username
		self.k = key

	def start_repl(self):
		ApplicationReplSession(self.u, self.k).check_auth()

		while True:
			expr = input("comando>")

			if expr == "sair":
				q = input("Deseja realmente sair?[Yy/Nn]")
				if q in "Yy":
					break
				else:
					continue

			elif expr == "SQL":
				query = input("query>")
				print("Aguarde, executando query...")
			elif expr == "gerar senha":
				senha = "a1234x"
				print("sua senha: ", senha)
				continue

			try:
				val = eval(expr)
				print(val)
			except Exception as e:
				print(e)

	def check_auth(self):
		if self.u == "usuario" and self.k == "10ab23ffx0":
			print("Logado! Iniciando Repl...")

		else:
			print("Desconectado, algo suspeito aconteceu! Tentativa de login suspeita.")
			print("ERRO: usuário ou senha são inconsistentes")
			exit()
			return 0





#code.interact(local=locals(), banner="REPL ftmpservice>")
# Temperatura.planilha() = banco de dados
#print('\n')
#print('~'*70)
#print('   No dia %i de %s, a variação de temperatura foi de %i° à %i°' % (a[1], Data.traducao(a[0]),Temperatura.planilha()[a[0] - 1][a[1] -1][1]['min'],Temperatura.planilha()[a[0] - 1][a[1] -1][1]['max']))
#print('~'*70)
#print('\n')

################################### IDEIA #######################################
def f():
	user = input("Insira o usuário: ")
	key  = input("Insira sua chave: ")
	repl_sess = ApplicationReplSession(user, key)
	return repl_sess.start_repl()

f()
#loop = asyncio.get_event_loop()
#loop.run_until_complete(f())
#loop.close()
#################################################################################
