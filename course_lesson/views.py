from django.shortcuts import render
from .models import *
# Create your views here.


def courses(request):
    return render(request, 'course_lesson/courses.html')


def course(request, course_id):
    course = Course.objects.get(id=course_id)
    modules = Module.objects.filter(course_id=course_id)
    teachers = Teacher.objects.filter(lessons__module__course_id=course_id)
    
    args = {
        'course': course,
        'modules': modules,
        'teachers': teachers,

    }
    return render(request, 'course_lesson/course.html', context=args)



def lesson(request, course_id, module_id, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    module = Module.objects.get(id=module_id)
    resources = Resource.objects.filter(lesson_id=lesson_id)
    lessons_from_module = Lesson.objects.filter(module_id=module_id)

    args = {
        'lesson': lesson,
        'module': module,
        'resources': resources,
        'lessons_from_module': lessons_from_module,

    }
    return render(request, 'course_lesson/lesson.html', context=args)


def course_end(request, course_id):
    return render(request, 'course_lesson/course_end.html')


