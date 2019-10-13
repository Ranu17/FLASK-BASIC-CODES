import pymysql
conn = pymysql.connect(host='localhost',user='root', password='project', db='banasthali')
a=conn.cursor()
query=''' insert into employee(eid, ename)
          values(101, 'ranu');'''

a.execute(query)
conn.commit()

