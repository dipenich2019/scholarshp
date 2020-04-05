import random
import sqlite3 as sql
from flask import request
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200)) 
   pin = db.Column(db.String(10))

   

   def __init__(self, name, city, addr,pin):
     
      self.name = name
      self.city = city
      self.addr = addr
      self.pin = pin

class present(db.Model):
    id = db.Column('present_id', db.Integer, primary_key = True)
    present = db.Column(db.String(100))
    description = db.Column(db.String(50))
 
    def __init__(self, present, description):
     
      self.present = present
      self.description = description
      
 


   
   
      

@app.route('/')
def show_all():
   return render_template('show_all.html', students = students.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         x=10
         pin =request.form['pin']
         random_with_N_digits(x)
         student = students(request.form['name'],request.form['city'], 
            request.form['addr'], pin=random_with_N_digits)
         
         db.session.add(student)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')



   def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)
   

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)