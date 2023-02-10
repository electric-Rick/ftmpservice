#from input_data import Data
#from gerador_temp.main import Temperatura
import asyncio
import sys
import time
from commands import commands

# adicionar modulo que lidará com login do usuário auth_module?
from code import InteractiveConsole

#from db.connection import Connection
class ApplicationReplSession:
	def __init__(self,username,key):
		self.u = username
		self.k = key

	def start_repl(self):
		if ApplicationReplSession(self.u, self.k).check_auth() == True:

		else:


		# checagem e interrupção
		# check--->OK continue por aqui >>>
		while True:
			#cabecalho da linha de comando
			expr = input("comando>")
			#rodapé da linha de comando
			if expr == "sair":
				q = input("Deseja realmente sair?[Yy/Nn]")
				if q in "Yy":
					break
				else:
					continue

			elif expr == 'SQL':
				query = input("query>")
				# Aqui você tenta encaixar a classe Connection com o método execute_query nesta parte do código
			elif expr == "gerar senha":
				senha = "a1234x"
				print("sua senha: ", senha)
				continue

			try:
				val = eval(expr)
				print(val)
			except Exception as e:
				print(e)

	def check_auth(self):  # Meta: Transformar em classe em sua respectiva pasta de módulo
		# Um loop para verificar uma lista de nomes e senhas através de dicionários
		if self.u == "usuario" and self.k == "1":
			print("Logado! Iniciando Repl...")
			return True

		else:
			# leva ao registro de usuário
			print("ERRO: usuário ou senha são inconsistentes OU não existe.")
			return False


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
