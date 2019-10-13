import pymysql
conn = pymysql.connect(host='localhost',user='root', password='project', db='banasthali')
a=conn.cursor()
query='select * from employee'
a.execute(query)
#lst=a.fetchall()
lst=a.fetchone()
print(lst)
for x in lst:
    print(x)
    
