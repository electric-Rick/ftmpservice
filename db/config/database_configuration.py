# Descrição: Arquivo irá alterar as variáveis de ambiente, carregará os módulos principais do banco.

import os
import sys
#sys.path.insert(0,'../')
from dotenv import dotenv_values

class ConfigureDatabase:
	def __init__(self, connection):
		self.c = connection
		pass

	def connection_params():
		config = dotenv_values("./.env") # Carrega as variáveis do .env
		print("Variáveis de ambiente carregadas")

		return { # JSON -> JavaScript Object Notation ---> API
			'user': config['USER'],
			'host': config['HOST'],
			'database': config['DATABASE'],
			'sec_k': config['PASSWORD'],
			'port': 3306
			 } # retorna um objeto com as variáves em formato JSON

	def wd_connection_params():
		config = dotenv_values("./.env")

		return {
			'user': config['USER'],
			'host': config['HOST'],
			'sec_k': config['PASSWORD'],
			'port': 3306
			}





