from django.urls import path
from .views import View_Courses

urlpatterns = [
    path('',View_Courses, name='View_Courses'),
]