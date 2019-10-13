import pymysql
from app import app
from app import module1
from flask import request,render_template
app.config["DEBUG"] = True


@app.route('/',methods=["GET", "POST"])
def adder_page():
    if request.method == "GET":
        return render_template('input.html')
    insert_emp1();
        


@app.route('/sec1.html',methods=["GET", "POST"])
def view_emp():
    if request.method == "POST":
        
        temp_drop= request.form.get("m")
        print(temp_drop)
        
        if temp_drop == 'eid':
            temp_id=int(request.form["tid"])
            result=module1.fetch_table_by_eid(temp_id)
            return render_template('output.html',abc=result)
        
        elif temp_drop == 'ename':
            temp_id=str(request.form["tid"])
            result=module1.fetch_table_by_ename(temp_id)
            return render_template('output.html',abc=result)

        elif temp_drop == 'dept_name':
            temp_id=str(request.form["tid"])
            result=module1.fetch_table_by_deptname(temp_id)
            return render_template('output.html',abc=result)

        elif temp_drop == 'dept_id':
            temp_id=str(request.form["tid"])
            result=module1.fetch_table_by_deptid(temp_id)
            return render_template('output.html',abc=result)

        else:
            temp_id=int(request.form["tid"])
            result=module1.fetch_table_by_salary(temp_id)
            return render_template('output.html',abc=result)        
        
    return render_template('sec1.html',title='Hello')


@app.route('/sec2.html',methods=["GET", "POST"])
def del_emp():
        if request.method == "POST":
        
            temp_drop= request.form.get("m")
            print(temp_drop)
            
            if temp_drop == 'eid':
                temp_id=int(request.form["tid"])
                result=module1.del_by_eid(temp_id)
                return render_template('output.html',abc=result)
            
            elif temp_drop == 'ename':
                temp_id=str(request.form["tid"])
                result=module1.del_by_ename(temp_id)
                return render_template('output.html',abc=result)

            elif temp_drop == 'dept_name':
                temp_id=str(request.form["tid"])
                result=module1.del_by_deptname(temp_id)
                return render_template('output.html',abc=result)

            elif temp_drop == 'dept_id':
                temp_id=str(request.form["tid"])
                result=module1.del_by_deptid(temp_id)
                return render_template('output.html',abc=result)

            else:
                temp_id=int(request.form["tid"])
                result=module1.del_by_salary(temp_id)
                return render_template('output.html',abc=result)
        return render_template('sec2.html',title='Hello')



@app.route('/sec3.html',methods=["GET", "POST"])
def insert_emp1():
    if request.method == "POST":
        #inputs = None
        temp_tid= int(request.form["tid"])
        temp_tname = str(request.form["tename"])
        temp_deptid=str(request.form["deptid"])
        temp_deptn=str(request.form["deptn"])
        salary=int(request.form["salary"])
        print("HELLLO")
        result=module1.insert_emp(temp_tid,temp_tname,temp_deptid,temp_deptn,salary)        
        return render_template('output1.html',abc=result)
    return render_template('sec3.html',title='hello')


@app.route('/sec4.html',methods=["GET", "POST"])
def update_emp():
        if request.method == "POST":
            temp_id=int(request.form["tid"])
            temp_name=str(request.form["tname"])
            result=module1.up_emp(temp_id, temp_name)       
        return render_template('sec4.html',title='Hello')    
    
        
                                
        
        
           
