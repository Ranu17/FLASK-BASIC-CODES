import pymysql
conn = pymysql.connect(host='localhost',user='root', password='project', db='banasthali')
a=conn.cursor()
query='select * from employee'
sql="update employee set ename='itsu' where eid=102"
a.execute(sql)
a.execute(query)
#lst=a.fetchall()
lst=a.fetchone()
print(lst)
for x in lst:
    print(x)
conn.commit()
