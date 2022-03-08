from flask import Flask, request, jsonify, Response
from flask_cors import CORS
#import json


app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def terraformGetOutput():
    data = 'Success!'

    #filedata = json.dumps(data)
    return data
