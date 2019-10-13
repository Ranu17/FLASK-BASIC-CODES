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
    
   
#from flask import render_template
from app import app
from flask import request,render_template
app.config["DEBUG"] = True

    
    

@app.route('/',methods=["GET", "POST"])
def adder_page():
    if request.method == "POST":
        inputs = None
        temp_tid= int(request.form["tid"])
        result=fetch_table(temp_tid)
        return render_template('output.html',abc=result)
    return render_template('input.html',title='Hello')

