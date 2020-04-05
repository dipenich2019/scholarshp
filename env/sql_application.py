from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('adult_students.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         student_id = request.form['student_Id']
        
         
         with sql.connect("sqlite3_database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO students (student_id,name,addr,city,pin) VALUES (?,?,?,?,?)",( student_id,nm,addr,city,pin) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result_new.html",msg = msg)
         con.close()



         

@app.route('/list')
def list():
   con = sql.connect("sqlite3_database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)

   

@app.route('/random')
def random():
   con = sql.connect("sqlite3_database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students s, Present p where s.student_id =p.ID ORDER BY random() LIMIT 2")
   
   rows = cur.fetchall()
   cur=con.execute("")
   return render_template("random.html",rows = rows)



if __name__ == '__main__':
   app.run(debug = True)


