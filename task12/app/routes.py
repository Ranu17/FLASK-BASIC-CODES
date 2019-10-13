import pymysql
from app import module1

   
#from flask import render_template
from app import app
from flask import request,render_template
app.config["DEBUG"] = True

    
    

@app.route('/',methods=["GET", "POST"])
def adder_page():
    if request.method == "POST":
        inputs = None
        temp_tid= int(request.form["tid"])
        result=module1.fetch_table(temp_tid)
        return render_template('output.html',abc=result)
    return render_template('input.html',title='Hello')

