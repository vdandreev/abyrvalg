#!/usr/bin/python
from flask import Flask
from flask_restful import Resource, Api, reqparse
import subprocess


app = Flask(__name__)
api = Api(app)

class MaritimeServer(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('whois', type=str, help='Request type. Will act on stress only')
        args = parser.parse_args()
              
        return {"I_AM": args.whois}


api.add_resource(MaritimeServer, '/')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
