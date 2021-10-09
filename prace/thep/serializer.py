from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        models = Student
        fields = [
            'name',
            'age'
        ]