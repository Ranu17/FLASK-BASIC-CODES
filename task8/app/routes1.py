from flask import request,render_template
from app import app

def calculate_result(str1):
    temp=str1*10
    return temp

@app.route('/',methods=["GET","POST"])
def adder_page():
    if request.method == "POST":
        inputs=None
        tnamea=str(request.form["tname"])
        result=calculate_result(tnamea)
        return render_template('output.html',abc=result)
    else:
        return render_template('input.html',title='hello')
                   
