from django.shortcuts import render

# Create your views here.


def courses(request):
    return render(request, 'course_lesson/courses.html')


def course(request, course_id):
    return render(request, 'course_lesson/course.html')


def lesson(request, course_id, module_id, lesson_id):
    return render(request, 'course_lesson/lesson.html')


def course_end(request, course_id):
    return render(request, 'course_lesson/course_end.html')


