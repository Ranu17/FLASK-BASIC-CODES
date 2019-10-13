import pymysql
	
def insert_table(temp_id,temp_name,temp_deptid,temp_deptn,salary):
    conn= pymysql.connect(host='localhost',user='root',
                      password='project', db='banasthali')
    a=conn.cursor()
    temp_str="INSERT INTO employee VALUES ("+ str(temp_id) +",'"+ temp_name +"','"+ temp_deptid +"','"+ temp_deptn +"',"+ str(salary) +")"
    a.execute(temp_str)
        
    conn.commit()
    str2="Value inserted."
    return str2



#from flask import render_template
from app import app
from flask import request,render_template
app.config["DEBUG"] = True

    
    

@app.route('/',methods=["GET", "POST"])
def adder_page():
    if request.method == "POST":
        inputs = None
        temp_tid= int(request.form["tid"])
        temp_tname = str(request.form["tename"])
        temp_deptid=str(request.form["deptid"])
        temp_deptn=str(request.form["deptn"])
        salary=int(request.form["salary"])
        result=insert_table(temp_tid,temp_tname,temp_deptid,temp_deptn,salary)        
        return render_template('output.html',abc=result)

    return render_template('input.html',title='Hello')

