from flask import Flask,jsonify,request
import  jpype     
import aspose.cells    
import json
from aspose.cells import Workbook
jpype.startJVM() 
workbook = Workbook(r"C:\Users\Juan\Downloads\data_challenge_files (2) (1) (1) (1) (2) (3) (1)\jobs.csv")
workbook.save(r"C:\Users\Juan\Downloads\data_challenge_files (2) (1) (1) (1) (2) (3) (1)\jobs.json")
jpype.shutdownJVM()
workbook = Workbook(r"C:\Users\Juan\Downloads\data_challenge_files (2) (1) (1) (1) (2) (3) (1)\departments.csv")
workbook.save(r"C:\Users\Juan\Downloads\data_challenge_files (2) (1) (1) (1) (2) (3) (1)\departments.json")
jpype.shutdownJVM()
workbook = Workbook(r"C:\Users\Juan\Downloads\data_challenge_files (2) (1) (1) (1) (2) (3) (1)\hired_employees.csv")
workbook.save(r"C:\Users\Juan\Downloads\data_challenge_files (2) (1) (1) (1) (2) (3) (1)\hired_employees.json")
jpype.shutdownJVM()
json_file_path = r"C:\Users\Juan\Downloads\data_challenge_files (2) (1) (1) (1) (2) (3) (1)\jobs.json"
with open(json_file_path, 'r') as j:
     jobs = json.loads(j.read())
json_file_path = r"C:\Users\Juan\Downloads\data_challenge_files (2) (1) (1) (1) (2) (3) (1)\departments.json"
with open(json_file_path, 'r') as j:
     departments = json.loads(j.read())
json_file_path = r"C:\Users\Juan\Downloads\data_challenge_files (2) (1) (1) (1) (2) (3) (1)\hired_employees.json"
with open(json_file_path, 'r') as j:
     hired_employees = json.loads(j.read())
app = Flask(__name__)
@app.route("/jobs")
def create_jobs():
    return jsonify(jobs)

@app.route("/departments")
def create_departments():
    return jsonify(departments)
@app.route("/hired_employees")
def create_hired_employees():
    return jsonify(hired_employees)


workbook = Workbook(r"C:\Users\Juan\OneDrive\Documentos\departments.csv")
workbook.save(r"C:\Users\Juan\OneDrive\Documentos\departments.json")
jpype.shutdownJVM()
json_file_path = r"C:\Users\Juan\OneDrive\Documentos\departments.json"
with open(json_file_path, 'r') as j:
     departments = json.loads(j.read())
app = Flask(__name__)
@app.route("/departments",methods=['POST'])
def create_jobs():
    return jsonify(departments)

if __name__ == '__main__':
    app.run(debug=True)