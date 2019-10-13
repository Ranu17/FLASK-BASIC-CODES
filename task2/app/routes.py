from app import app

@app.route('/')
@app.route('/index')
def index():
    user={'username':'RANU'}
    return '''
<html>
    <head>
        <title>MY PAGE</title>
    </head>
    <body bgcolor="pink" align="center">
        <h1>Hello, ''' + user['username'] + ''' </h1>
    </body>
</html>'''
