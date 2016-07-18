from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    context = { "courses" : Course.objects.all()}
    return render(request, 'coursesapp/index.html', context)

def addcourse(request):
    Course.objects.create(course_name=request.POST['course_name'], description=request.POST['description'])
    return redirect('/')
