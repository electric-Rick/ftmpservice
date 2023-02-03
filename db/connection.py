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
		db = pymysql.connect(host=self.h, user=self.u, password=self.p, database=self.d, port=3306)
		cursor = db.cursor()
		print("Conectado")

	def execute_query(self, query):
		sql = query
		pass

def _create_connection(self):
	return Connection(host=self._host,
			  user=self._user,
                          password=self._password,
                          database=self._database,
                          port=self._port,
                          charset=self._charset,
                          cursorclass=self._cursor_class,
                          **self._other_kwargs)

PASSWORD='giselemeuamor'
HOST='0.0.0.0'
USER='root'
DATABASE='test_yoobe'

a = PASSWORD
b = HOST
c = USER
d = DATABASE

f = Connection(a, b, c ,d)
print(f.to_database())

print(f)



