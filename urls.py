#URLs

# grading_system/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.grading_system, name='grading_system'),
]