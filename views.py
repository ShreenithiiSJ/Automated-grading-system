#views

# gradingapp/views.py

from django.shortcuts import render
from .models import GradingData

def grading_system(request):
    data = GradingData.objects.all()
    return render(request, 'grading_system.html', {'data': data})