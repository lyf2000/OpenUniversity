from django.shortcuts import render

# Create your views here.


def courses(request):
    pass


def course(request, course_id):
    pass


def lesson(request, course_id, module_id, lesson_id):
    return render(request, 'course_lesson/lesson.html')


def course_end(request, course_id):
    pass


