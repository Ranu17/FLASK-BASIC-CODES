from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user1={'username':'DIVU'}
    return render_template('index.html', user=user1) # title='Home',

