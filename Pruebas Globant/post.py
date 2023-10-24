from flask import Flask,jsonify,request
import  jpype     
import aspose.cells    
import json
from aspose.cells import Workbook

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
