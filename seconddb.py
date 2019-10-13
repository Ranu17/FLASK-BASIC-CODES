import pymysql
conn = pymysql.connect(host='localhost',user='root', password='project', db='banasthali')
a=conn.cursor()
query='''create table Employee
         (eid int(4) NOT NULL,
         ename VARCHAR(20));'''

a.execute(query)
conn.commit()

