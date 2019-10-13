import pymysql
conn = pymysql.connect(host='localhost',user='root', password='project')
a=conn.cursor()
query='drop database CEBS'

a.execute(query)
conn.commit()
