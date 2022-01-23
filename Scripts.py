import pymssql

conn = pymssql.connect(host=['localhost'], user=['postgres'], password=['admin'],database=['db_alkemy'], port=['5432'])
cur = conn.cursor()
try:
	cur.execute('Scripts.sql')
	conn.commit()
except Exception as e:
	print(e)
	conn.rollback()
cur.close()
conn.close()
















