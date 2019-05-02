from django.http import HttpResponse
from django.shortcuts import render
import math
from . import helper
from .models import *


# Create your views here.


def courses(request):
    courses = Course.objects.all()
    args = {
        'courses': courses,
    }
    return render(request, 'course_lesson/courses.html', context=args)


def course(request, course_queue):
    try:
        course = Course.objects.get(queue_number=course_queue)
        modules = Module.objects.filter(course_id=course.id).order_by('queue_number')
        teachers = Teacher.objects.filter(lessons__module__course_id=course.id)
        teachers = set(teachers)

        args = {
            'course': course,
            'modules': modules,
            'teachers': teachers,

        }
        return render(request, 'course_lesson/course.html', context=args)
    except Course.DoesNotExist:
        return HttpResponse(helper.page_not_found('course', course_queue))


def lesson(request, course_queue, module_queue, lesson_queue):
    try:
        course = Course.objects.get(queue_number=course_queue)
        module = Module.objects.get(course_id=course.id, queue_number=module_queue)
        lesson = Lesson.objects.get(module_id=module.id, queue_number=lesson_queue)
        try:
            next_lesson = Lesson.objects.get(module_id=module.id, queue_number=lesson_queue+1)
        except Lesson.DoesNotExist:
            next_lesson = None
# might be empty:
        resources = Resource.objects.filter(lesson_id=lesson.id)
        lessons_from_module = Lesson.objects.filter(module_id=module.id).order_by('queue_number')

        args = {
            'lesson': lesson,
            'module': module,
            'resources': resources,
            'lessons_from_module': lessons_from_module,
            'next_lesson': next_lesson,
        }
        return render(request, 'course_lesson/lesson.html', context=args)
    except Course.DoesNotExist:
        return HttpResponse(helper.page_not_found('course', course_queue))
    except Module.DoesNotExist:
        return HttpResponse(helper.page_not_found('module', module_queue))
    except Lesson.DoesNotExist:
        return HttpResponse(helper.page_not_found('lesson', lesson_queue))


def course_end(request, course_id):
    return render(request, 'course_lesson/course_end.html')
