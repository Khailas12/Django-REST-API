from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from thep.serializers import StudentSerializers
from thep.models import Student



class Practice(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        serializer = StudentSerializers(queryset, many=True)    # many=True is used to serialize the queryset or list of objects instead of a single object instance    
        return Response(serializer.data)
    
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)