from flask import Flask
from flask_restful import request ,Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)

class TimestampServiceNull(Resource):
    def get(self):
        parsed_date = datetime.utcnow()
        return { "utc" : datetime.strftime(parsed_date, "%a, %d %b %Y %H:%M:%S GMT" ),
                "unix": int((datetime.timestamp(parsed_date) - datetime.timestamp(datetime.strptime("1970-01-01", "%Y-%m-%d")))*1000)
                }

class TimestampService(Resource):
    def get(self, received_date):
        try:
            parsed_date = datetime.strptime(received_date, "%Y-%m-%d")
            return { "utc" : datetime.strftime(parsed_date, "%a, %d %b %Y %H:%M:%S GMT" ),
                     "unix": int((datetime.timestamp(parsed_date) - datetime.timestamp(datetime.strptime("1970-01-01", "%Y-%m-%d")))*1000)
                    }
        except:
            try:
                parsed_unix = int(received_date)
                date_parsed =  datetime.utcfromtimestamp(parsed_unix/1000)
                return { "utc" : datetime.strftime(date_parsed, "%a, %d %b %Y %H:%M:%S GMT" ),
                     "unix": parsed_unix
                    }
            except:
                return {"error" : "Invalid Date" }
            
        
api.add_resource(TimestampServiceNull, '/api/')
api.add_resource(TimestampService, '/api/<string:received_date>')

if __name__ == '__main__':
    app.run(debug=True)