from flask import Flask
from flask import render_template
from flask import jsonify
from flask import Flask, render_template, request, redirect, Response, jsonify
import mysql.connector
import time


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="string"
)
mycursor = mydb.cursor()
app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/search')
def search():
  return render_template('search.html')

@app.route('/search_process')
def search_process():
  try:
    string = request.args.get('string', 0, type=str)
    if string.isnumeric():
      sql="insert into string_tbl(num,alpha,alpha_num) values(%s,%s,%s)"  
      val = [string,"",""]
      print(val)
      print(sql)
      mycursor.execute(sql,val)  
      mydb.commit()
      return jsonify(result="numerics")

    elif string.isalpha():
      sql="insert into string_tbl(num,alpha,alpha_num) values(%s,%s,%s)"  
      val = ["",string,""]
      print(val)
      print(sql)
      mycursor.execute(sql,val)   
      mydb.commit()
      return jsonify(result="alphabets")

    elif string.isalnum():
      sql="insert into string_tbl(num,alpha,alpha_num) values(%s,%s,%s)"  
      val = ["","",string]
      print(val)
      print(sql)
      mycursor.execute(sql,val)   
      mydb.commit()
      return jsonify(result="alphanumerics")

  except Exception as e:
    return str("exception")