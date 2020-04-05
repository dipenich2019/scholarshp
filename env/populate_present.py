
from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)



@app.route('/')
def new_present():
   return render_template('present.html')  

@app.route('/present',methods = ['POST', 'GET'])
def present():
   if request.method == 'POST':
      try:
         gift = request.form['gift']
         description = request.form['description']
         present_id = request.form['present_id']
        
                
         with sql.connect("sqlite3_database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO Present (ID,GIFT,DESCRIPTION) VALUES (?,?,?)",( present_id,gift, description) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
     

         return render_template("result_new.html", msg = msg)
         con.close()

if __name__ == '__main__':
   app.run(debug = True)