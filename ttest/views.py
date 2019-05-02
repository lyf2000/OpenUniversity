from django.shortcuts import render
from .models import MyTest
from .models import Question
from course_lesson.models import Module
from course_lesson.models import Course
from .forms import TestForm

# Create your views here.


def test(request, course_queue, module_queue):
    print("Я ЗАШЕЛ СЮДА++")
    course = Course.objects.get(queue_number=course_queue)
    module = Module.objects.get(queue_number=module_queue, course_id=course.id)
    test = module.test
    print('test', test)
    mytest = MyTest.objects.create(test=test, module=module) #Создает мой тест
    questions = Question.objects.filter(test=test)
    print('questions', questions)
    print('here')
    testform = TestForm(questions=questions)
    print("TestForm", testform)
    print("hello")
    return render(request, 'ttest/test.html', {"form": testform})

def test_result(request, course_queue, module_queue):
    return render(request, 'ttest/test_result.html')

# def test(request):
#     return render(request, 'ttest/tests.html')

# def test_result(request):
#     return render(request, 'ttest/resultsTests.html')

