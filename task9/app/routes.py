import pymysql

def insert_table(tid, tname):
    conn=pymysql.connect(host='localhost', user='root',password='project',db='banasthali')
    a=conn.cursor()
    temp_str="insert into employee values ("+str(tid) +",'" + tname+"')"
    
    a.execute(temp_str)
    conn.commit()
    print('saved')
    str2="Value inserted"
    return str2


from app import app
from flask import request,render_template
app.config["DEBUG"] = True


@app.route('/',methods=["GET","POST"])
def adder_page():
    if request.method == "POST":
        inputs=None
        temp_tid=int(request.form["tid"])
        temp_tname=str(request.form["tname"])
        result=insert_table(temp_tid,temp_tname)
        return render_template('output.html',abc=result)
    return render_template('input.html',title='hello')
                   
