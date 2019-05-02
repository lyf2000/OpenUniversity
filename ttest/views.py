from django.shortcuts import render
from .models import Test
from .models import Question
from course_lesson.models import Module
from course_lesson.models import Course

# Create your views here.


def test(request, course_queue, module_queue):
    course = Course.objects.get()
    return render(request, 'ttest/test.html')

def test_result(request, course_queue, module_queue):
    return render(request, 'ttest/test_result.html')

# def test(request):
#     return render(request, 'ttest/tests.html')

# def test_result(request):
#     return render(request, 'ttest/resultsTests.html')

