from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from course_lesson.models import  *
# Create your views here.


def index(request):
    courses = Course.objects.all()
    return render(request, 'pages/index.html', {'courses':courses})



