import pymysql
conn = pymysql.connect(host='localhost',user='root', password='project', db='banasthali')
a=conn.cursor()
lst=[(102,'darsh'),
    (103,'vaishu'),
     (104,'divu'),
     (105,'priyanka')]
query=''' insert into employee(eid, ename)
          values(%s,%s);'''

a.executemany(query,lst)
conn.commit()

