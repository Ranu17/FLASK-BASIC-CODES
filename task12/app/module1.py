import pymysql
	
def insert_table(tid,tname):
    conn= pymysql.connect(host='localhost',user='root',
                      password='project', db='banasthali')
    a=conn.cursor()
    temp_str="INSERT INTO employee VALUES ("+ str(tid) +",'"+ tname +"')"
    a.execute(temp_str)
        
    conn.commit()
    str2="Value inserted."
    return str2

def fetch_table(str1):
    conn= pymysql.connect(host='localhost',user='root',
                      password='project', db='banasthali')
    a=conn.cursor()
    temp_str="select * from employee where eid="+ str(str1)+";"
    a.execute(temp_str)
    lst=a.fetchall()
    print(lst)
    return lst
    
