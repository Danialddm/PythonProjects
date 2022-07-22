from flask import Flask, request
from flask_restful  import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import pyodbc

# DB connection
server = '10.192.63.52\DWH01,49149' 
print(server)
database = 'WebSiteDB' 
username = 'websiteuser' 
password = 'B$tor$4416#Bos' 
cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};"
                        "SERVER= GIG001VERP02;"#10.192.63.52\DWH01,49149;"
                        "DATABASE= OKDynAXTest;"#WebSiteDB;"
                        #"UID= websiteuser;"
                        #"PWD= B$tor$4416#Bos;"
                        "Trusted_Connection=yes;")
cursor = cnxn.cursor()
conn = pyodbc.connect()

app = Flask(__name__)
api = Api(app)

class Ids(Resource):
    def get(self):
        return {'ids': [1,2,3]}

api.add_resource(Ids, '/ids') 

if __name__ == '__main__':
     app.run(port='5002')

