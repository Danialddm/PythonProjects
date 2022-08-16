from flask import Flask, jsonify, request
  
app = Flask(__name__)
#app.config['SERVER_NAME'] = 'api.amiracs.com' 
  
@app.route('/', methods=['GET'])
def helloworld():
    if(request.method == 'GET'):
        data = {"data": "Hello Masoud...."}
        return jsonify(data)
  
  
if __name__ == '__main__':
    #app.config['SERVER_NAME'] = 'amiracs.com' 
    #app.url_map.default_subdomain = 'api'
    #app.run(host=app.config["SERVER_NAME"],debug=True)
    app.run(port=9010)