from django.contrib import admin
from.models import Student
from.models import Students
@admin.register(Student)
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'marks', 'email')