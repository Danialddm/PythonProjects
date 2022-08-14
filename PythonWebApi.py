from flask import Flask, request, session
from flask_restful  import Resource, Api, reqparse
from json import dumps
from flask_jsonpify import jsonify
import pyodbc

# DB connection
server = '10.192.63.52\DWH01,49149'#'172.31.3.245'# 
database = 'WebSiteDB'#'OKDynAXTest'# 
username = 'websiteuser'#'lotteryuser'# 
password = 'B$tor$4416#Bos'#'123'# 
cnxn = pyodbc.connect(r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.192.63.52\DWH01,49149;DATABASE=WebSiteDB;UID=websiteuser;PWD=B$tor$4416#Bos')
cursor = cnxn.cursor()
results = []

app = Flask(__name__)
api = Api(app)

token = "jF4OtLztYvs4S8jdAsswv6ut96yMTbkV"
headers = {
"accept" : "application/json",
"Authorization": str(token)
}


@app.route('/invent/get_itemid', methods = ['GET'])
def get_itemid():
    try:
        itemid = request.args.getlist('itemid', type = str)
        headers = request.headers
        auth = headers.get("token")
        if auth == token:
            for x in itemid:        
                query = cursor.execute("select itemid,AvailPhysical,storeid from [dbo].[OnHandItemsStock] where itemid=" + x)
                columns = [column[0] for column in cursor.description]
                for row in cursor.fetchall():
                    results.append(dict(zip(columns, row)))
            results.append({'success' : 'true'})
            return (jsonify(results)), 200
        else:
            return jsonify({'message' : 'Token is invalid!', 'success' : 'false'}),401
    except:
        return jsonify({'error' : 'bad request', 'success' : 'false'}) , 400

@app.route('/invent/get_batch', methods = ['GET'])
def get_batch():
    try:
        num = int(request.args.get('num'))
        headers = request.headers
        auth = headers.get("token")
        
        if auth == token:
            query = cursor.execute("select top " + str(num) + "itemid,AvailPhysical,storeid from [dbo].[OnHandItemsStock] order by itemid desc")
            columns = [column[0] for column in cursor.description]
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            results.append({'sucess' : 'true'})
            return jsonify(results)
        else:
            return jsonify({'message' : 'Token is invalid!', 'success' : 'false'}),401
    except:
        return jsonify({'error' : 'bad request', 'success' : 'false'}) , 400

@app.route('/invent/get_storeid', methods = ['GET'])
def get_storeid():
    try:
        storeid = request.args.get('storeid', type = str)
        headers = request.headers
        auth = headers.get("token")
        if auth == token:
            query = cursor.execute("select itemid,AvailPhysical,storeid from [dbo].[OnHandItemsStock] where storeid=" + storeid)
            columns = [column[0] for column in cursor.description]
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            results.append({'sucess' : 'true'})
            return jsonify(results)
        else:
            return jsonify({'message' : 'Token is invalid!', 'success' : 'false'}),401
    except:
        return jsonify({'error' : 'bad request', 'success' : 'false'}) , 400

@app.route('/invent/get_allitemid', methods = ['GET'])
def get_Allitemid():
    try:
        headers = request.headers
        auth = headers.get("token")
        if auth == token:
            query = cursor.execute("select itemid,AvailPhysical,storeid from [dbo].[OnHandItemsStock] order by itemid desc")
            columns = [column[0] for column in cursor.description]
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            results.append({'sucess' : 'true'})
            return jsonify(results)
        else:
            return jsonify({'message' : 'Token is invalid!', 'success' : 'false'}),401
    except:
        return jsonify({'error' : 'bad request', 'success' : 'false'}) , 400

if __name__ == '__main__':
     #app.run(host='127.0.0.1', port='5002')
     app.run(host='0.0.0.0',port=9010)

