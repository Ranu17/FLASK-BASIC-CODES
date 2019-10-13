from flask import request
from app import app

def calculate_result(str1):
    temp=str1*10
    return temp

@app.route('/', methods=["GET", "POST"])
def adder_page():
    if request.method == "POST" :
        input = None
        tname = str(request.form["tname"])
        result = calculate_result(tname)

        str1 = ''' <html>
                  <head><title></title></head>
                  <body>
                    <p>{abc}</p>
                    <p><a href = "/">Click here to see details again</a></p>
                  </body>
                  </html>'''.format(abc=result)
        return str1
    return ''' <html>
                  <head><title></title></head>
                  <body>
                    <p>Enter name of twitter account:</p>
                    <form method="post" action="#">
                        <p><input type="text" name="tname" /></p>
                        <p><input type="submit" value="See Details" /></p>
                    </form>
                    
                  </body>
                  </html>'''

