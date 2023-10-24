import requests
import mysql.connector
url= 'http://127.0.0.1:5000/jobs'
jobs = requests.get(url).json()
url= 'http://127.0.0.1:5000/hired_employees'
hired_employees = requests.get(url).json()
url= 'http://127.0.0.1:5000/departments'
departments = requests.get(url).json()
conn = mysql.connector.connect(host='localhost',password='1234',user='root',database = 'api')
if conn.is_connected():
    print('Connection establieshed')
cursor = conn.cursor()
cursor.execute("CREATE TABLE jobs(id varchar(100) ,name varchar(100))")
cursor.execute("CREATE TABLE departments(id varchar(100) ,name varchar(100))")
cursor.execute("CREATE TABLE hired_employees(id varchar(100) ,name varchar(100), date varchar(100),deparment varchar(100),job varchar(100))")
for i in jobs:
    id = i.get('id')
    name  = i.get('name')
    cursor.execute("insert into jobs(id,name) values(%s, %s)",(id,name))
for i in departments:
    id = i.get('id')
    name  = i.get('name')
    cursor.execute("insert into departments(id,name) values(%s, %s)",(id,name))
for i in hired_employees:
    id = i.get('id')
    name  = i.get('name')
    date = i.get('date')
    deparment = i.get('deparment')
    job = i.get('job')
    cursor.execute("insert into hired_employees(id,name,date,deparment,job) values(%s, %s,%s, %s,%s)",(id,name,date,deparment,job))
conn.commit()