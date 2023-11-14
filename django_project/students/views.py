from django.shortcuts import render
from .models import student
def index(request):
    return render(request,'students/index.html',{
        'students':student.objects.all()
    })