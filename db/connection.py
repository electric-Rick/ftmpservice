import os
import sys
import pymysql # banco de dados
#import mysql.connector # banco de dados
from config.database_configuration import ConfigureDatabase




class Connection:
	def __init__(self, database, table):
		self.d = database # 1998
		self.t = table
		pass

	def to_database(a,b,**kwargs): # ['agosto', 'julho', 'dezembro','janeiro']
		global t
		global d

		t = a
		d = b

		try:
			if t == None and d == None:
				dc = ConfigureDatabase.connection_params() #carregar_parametros_de_conexão()
				db  = pymysql.connect(host=dc['host'], user=dc['user'], password=dc['sec_k'], database=dc['database'], port=dc['port'])			
				cursor =db.cursor()
#				return cursor
				# tratar as próximas classes de insert, delete, update, read
			else:
				dc = ConfigureDatabase.wd_connection_params()
				db = pymysql.connect(host=dc['host'], user=dc['user'], password=dc['sec_k'], database=d, port=dc['port'])
				cursor = db.cursor()
#				return cursor
				# tratar as próximas classes de insert, delete, update e read.
		except:
			print("DB_ERR: Erro de conexão.")
			raise Exception
		finally:
#			db.close()
			print("Fim da conexão com o banco de dados. \n TABLE: ", t, "\n DATABASE:  ", d)

	def execute_query(query):
		print("QUERY CHAMADA: ", query)
		cursor = Connection.to_database('database', 'test_yoobe')
		pass




db = Connection("formiga","lazer")
print(db)
