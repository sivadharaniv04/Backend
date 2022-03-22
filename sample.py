from flask import Flask,request
import sqlite3
 
 
app=Flask(__name__)
@app.get('/')
def function1():
    return "Student details"
 
@app.post('/h')
def function2():
    con=sqlite3.Connection("C:/Users/trc/Documents/Nightskill/sample.db")
    cur=con.cursor()
    data=request.get_json()
    name=data["Name"]
    rollno=data["Rollno"]
    mark=data["Mark"]
 
    stu_detail=(name,rollno,mark)
    cur.execute("create table if not exists stu_detail(Name varchar(40),Rollno varchar(40),Mark int)")
    cur.execute("insert into stu_detail values (?,?,?)",stu_detail)
    con.commit()
    con.close()
    print(data)
    return "we got the data"
 
@app.patch("/upd")
def update():
    data=request.get_json()
    updates(data)
    return("Updated")

def updates(data):
    con=sqlite3.Connection("C:/Users/trc/Documents/Nightskill/sample.db")
    query=f'update stu_detail set Name="{data["Name"]}" where Rollno = "{data["Rollno"]}"'
    cur=con.cursor()
    cur.execute(query)
    con.commit()


@app.delete("/delete/<Rollno>")
def delete(Rollno):
    delete(Rollno)
    return("Deleted")

def delete(Rollno):
    con=sqlite3.Connection("C:/Users/trc/Documents/Nightskill/sample.db")
    query=f'delete from stu_detail where Rollno="{Rollno}"'
    cur=con.cursor()
    cur.execute(query)
    con.commit()
app.run(debug=True)