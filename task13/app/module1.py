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

def fetch_table_by_eid(str1):
    conn= pymysql.connect(host='localhost',user='root',
                      password='project', db='banasthali')
    a=conn.cursor()
    temp_str="select * from employee where eid="+ str(str1)+";"
    a.execute(temp_str)
    lst=a.fetchall()
    print(lst)
    return lst


def fetch_table_by_ename(str1):
    conn= pymysql.connect(host='localhost',user='root',
                      password='project', db='banasthali')
    a=conn.cursor()
    temp_str="select * from employee where ename='"+ str(str1)+"';"
    a.execute(temp_str)
    lst=a.fetchall()
    print(lst)
    return lst


def fetch_table_by_deptname(str1):
    conn= pymysql.connect(host='localhost',user='root',
                      password='project', db='banasthali')
    a=conn.cursor()
    temp_str="select * from employee where department_name='"+ str(str1)+"';"
    a.execute(temp_str)
    lst=a.fetchall()
    print(lst)
    return lst

def fetch_table_by_deptid(str1):
    conn= pymysql.connect(host='localhost',user='root',
                      password='project', db='banasthali')
    a=conn.cursor()
    temp_str="select * from employee where department_id='"+ str(str1)+"';"
    a.execute(temp_str)
    lst=a.fetchall()
    print(lst)
    return lst

def fetch_table_by_salary(str1):
    conn= pymysql.connect(host='localhost',user='root',
                      password='project', db='banasthali')
    a=conn.cursor()
    temp_str="select * from employee where salary="+ str(str1)+";"
    a.execute(temp_str)
    lst=a.fetchall()
    print(lst)
    return lst

def del_by_eid(str1):
    conn= pymysql.connect(host='localhost',user='root',
                      password='project', db='banasthali')
    a=conn.cursor()
    temp_str="delete from employee where eid="+ str(str1)+ ";"
    a.execute(temp_str)
    conn.commit()
    lst=a.fetchall()
    return lst


def del_by_ename(str1):
    conn= pymysql.connect(host='localhost',user='root',
                      password='project', db='banasthali')
    a=conn.cursor()
    temp_str="delete from employee where ename='"+ str(str1)+ "';"
    a.execute(temp_str)
    conn.commit()
    lst=a.fetchall()
    return lst

def del_by_deptname(str1):
    conn= pymysql.connect(host='localhost',user='root',
                      password='project', db='banasthali')
    a=conn.cursor()
    temp_str="delete from employee where department_name='"+ str(str1)+"';"
    a.execute(temp_str)
    lst=a.fetchall()
    conn.commit()
    print(lst)
    return lst

def del_by_deptid(str1):
    conn= pymysql.connect(host='localhost',user='root',
                      password='project', db='banasthali')
    a=conn.cursor()
    temp_str="delete from employee where department_id='"+ str(str1)+"';"
    a.execute(temp_str)
    conn.commit()
    lst=a.fetchall()
    print(lst)
    return lst

def del_by_salary(str1):
    conn= pymysql.connect(host='localhost',user='root',
                      password='project', db='banasthali')
    a=conn.cursor()
    temp_str="delete from employee where salary="+ str(str1)+";"
    a.execute(temp_str)
    conn.commit()
    lst=a.fetchall()
    print(lst)
    return lst


def insert_emp(temp_id,temp_name,temp_deptid,temp_deptn,salary):
    print("1")
    conn= pymysql.connect(host='localhost',user='root',
                      password='project', db='banasthali')
    a=conn.cursor()
    #temp_str="INSERT INTO employee VALUES ("+ str(temp_id) +",'"+ temp_name +"','"+ temp_deptid +"','"+ temp_deptn +"',"+ str(salary) +")"
    temp_str="INSERT INTO employee VALUES ("+ str(temp_id) +",'"+ temp_name +"','"+ str(temp_deptid) +"','"+ temp_deptn +"',"+ str(salary) +")"
    a.execute(temp_str)
        
    conn.commit()
    str2="Value inserted."
    return str2




    
    
