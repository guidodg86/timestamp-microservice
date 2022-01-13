from json.decoder import JSONDecodeError
from flask import Flask
from flask_restful import request ,Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

class TimestampService(Resource):
    def get(self):
        return {"message": "test"}

api.add_resource(TimestampService, '/')

if __name__ == '__main__':
    app.run(debug=True)