from flask import Flask, request
from flask_restful  import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import pyodbc

# DB connection
server = '172.31.3.245'#'10.192.63.52\DWH01,49149' 
print(server)
database = 'OKDynAXTest'#'WebSiteDB' 
username = 'lotteryuser'#'websiteuser' 
password = '123'#'B$tor$4416#Bos' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
query = cursor.execute("select top 10 itemid,qty from retailtransactionsalestrans;")
columns = [column[0] for column in cursor.description]
results = []
for row in cursor.fetchall():
    results.append(dict(zip(columns, row)))

#result = {'data': [dict(zip(tuple (query) ,i)) for i in cursor]}




app = Flask(__name__)
api = Api(app)

class ItemID(Resource):
    def get(self):
        return jsonify(results)

api.add_resource(ItemID, '/itemid') 

if __name__ == '__main__':
     app.run(port='5002')

