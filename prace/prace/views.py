from rest_framework.views import APIView
from rest_framework.response import Response
from thep.serializer import StudentSerializers
from thep.models import Student



class Practice(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'bruce wayne',
            'age': 20,
            'place': 'gotham',
        }
        return Response(data)
    
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)