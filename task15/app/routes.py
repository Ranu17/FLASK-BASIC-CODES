from app import app
from flask import request,render_template

@app.route('/',methods=["GET", "POST"])
def myindex():
    if request.method == "GET":
        return render_template('index.html')
