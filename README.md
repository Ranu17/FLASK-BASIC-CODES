# FLASK-BASIC-CODES
BASIC IMPLEMENTATION OF BACK-END USING FLASK AND PYTHON

INSTALL PYTHON 3 OR ABOVE. RUN THE .PY FILE IN THE COMMAND PROMPT BY CREATING A VIRTUAL ENVIRONMENT:
1. CREATE A FOLDER (EXAMPLE-FOLD1)
2. INSTALL VIRTUALENV ------  pip install virtualenv 
3. INSTALL SCRIPTS
4. COPY ONE TASK FOLDER HERE
5. ON CMD CHANGE DIRECTORY TO FOLD1 AND RUN SCRIPTS\ACTIVATE
6. INSTALL FLASK ------ pip install flask
7. CHANGE TO DESIRED TASK FOLDER
8. RUN ----- flask run



FROM TASK10 THE CODE INVOLVES DATABASE AS WELL USING MYSQL. THE DATABASE IS MADE IN THE MYSQL SOFTWARE AND THEN QUERIED USING FLASK.
conn= pymysql.connect(host='localhost',user='root',password='project', db='banasthali')
<<<<<<<     CREATE YOUR OWN USER AND PASSSWORD ATTRIBUTES IN MYSQL      >>>>>>>>
DATABASE NAME: banasthali
TABLE NAME: employee
FIELDS:
eid (int(4))
ename (varchar(20))
