from rest_framework import serializers
from .models import Student
from .models import Students
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = '__all__'                
class studentsSerualizers(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields='__all__'    