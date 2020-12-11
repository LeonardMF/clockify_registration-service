import json
from flask import Flask, jsonify, request, Response
from flask_cors import CORS

from functions.lambda_function import lambda_handler
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def handleGetRequest():

    event_obj = {
        'httpMethod':'GET'
    }
    
    respond_json = lambda_handler(event=event_obj, context={})
    
    return json.loads(respond_json['body']), respond_json['statusCode']

@app.route('/', methods=['POST'])
def handlePostRequest():

    event_obj = {
        'body': request.data.decode('utf-8'),
        'httpMethod':'POST'
    }

    respond_json = lambda_handler(event=event_obj, context={})

    return json.loads(respond_json['body']), respond_json['statusCode']

if __name__ == '__main__' :
    app.run(host="0.0.0.0",debug=True)