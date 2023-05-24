# Response structure
from rest_framework.response import Response

def responce(status,message,data):
    res = {"status":status,"message":message,"data":data}
    return Response(res)