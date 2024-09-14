from.models import Student
from.models import Students
from.serializers import StudentSerializers
from.serializers import studentsSerualizers
from rest_framework import viewsets

class studentModelViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    
class studentsModelViewset(viewsets.ModelViewSet):
    queryset=Students.objects.all()
    serializer_class=studentsSerualizers  

