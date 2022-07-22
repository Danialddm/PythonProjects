from flask import Flask, request
from flask_restful  import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import pyodbc

# DB connection
server = '172.31.3.245'#'10.192.63.52\DWH01,49149' 
database = 'OKDynAXTest'#'WebSiteDB' 
username = 'lotteryuser'#'websiteuser' 
password = '123'#'B$tor$4416#Bos' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
results = []

app = Flask(__name__)
api = Api(app)

@app.route('/get')
#class ItemID(Resource):
def get():
    itemid = request.args.get('itemid')
    query = cursor.execute("select itemid,qty from retailtransactionsalestrans where itemid=" + itemid)
    columns = [column[0] for column in cursor.description]
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return jsonify(results)

#api.add_resource(ItemID, '/itemid') 

if __name__ == '__main__':
     app.run(port='5002')

