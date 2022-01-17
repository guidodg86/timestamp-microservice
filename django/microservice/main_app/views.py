from django.shortcuts import render
from rest_framework.views import APIView
from datetime import datetime
from rest_framework.response import Response

class TimestampServiceNull(APIView):

    def get(self, request):
        parsed_date = datetime.utcnow()
        return Response({ "utc" : datetime.strftime(parsed_date, "%a, %d %b %Y %H:%M:%S GMT" ),
                "unix": int((datetime.timestamp(parsed_date) - datetime.timestamp(datetime.strptime("1970-01-01", "%Y-%m-%d")))*1000)
                })

class TimestampService(APIView):

    def get(self, request, received_date):
        try:
            parsed_date = datetime.strptime(received_date, "%Y-%m-%d")
            return Response({ "utc" : datetime.strftime(parsed_date, "%a, %d %b %Y %H:%M:%S GMT" ),
                     "unix": int((datetime.timestamp(parsed_date) - datetime.timestamp(datetime.strptime("1970-01-01", "%Y-%m-%d")))*1000)
                    })
        except:
            try:
                parsed_unix = int(received_date)
                date_parsed =  datetime.utcfromtimestamp(parsed_unix/1000)
                return Response({ "utc" : datetime.strftime(date_parsed, "%a, %d %b %Y %H:%M:%S GMT" ),
                     "unix": parsed_unix
                    })
            except:
                return Response({"error" : "Invalid Date" })