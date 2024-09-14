from django.contrib import admin
from django.urls import path, include
from API import views
from rest_framework.routers import DefaultRouter

# Create router object
router = DefaultRouter()

# Register StudentModelViewSet with router
router.register('studentapi', views.studentModelViewset, basename="student")
router.register('stusapi', views.studentsModelViewset, basename="students")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), # Include router URLs directly
]


