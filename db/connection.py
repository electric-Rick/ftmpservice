import os
import pymysql


class Connection:
	def __init__(self, username, host, database, password):
		self.u = username
		self.h = host
		self.d = database
		self.p = password
		pass

	def to_database(self):
		db = pymysql.connect(host=self.h, user=self.u, password=self.p, database=self.d, port='')
		cursor = db.cursor()
		print("Conectado")

	def execute_query(self, query):
		sql = query



PASSWORD=''
HOST=''
USER='root'
DATABASE='test_yoobe'

a = PASSWORD
b = HOST
c = USER
d = DATABASE

f = Connection(a, b, c ,d)
#print(f.to_database())

print(f)
