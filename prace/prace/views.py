from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from thep.serializers import StudentSerializers
from thep.models import Student
from rest_framework.permissions import IsAuthenticated


class Practice(APIView):
    
    permission_classes = (IsAuthenticated, )    # denies unauthenticated user
    
    def get(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        student1 = queryset.first()     # this gives the restult one by one rather than all.
        serializer = StudentSerializers(student1)   
        return Response(serializer.data)
    
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
# many=True is used to serialize the queryset or list of objects instead of a single object instance  