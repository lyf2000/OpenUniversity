from django.urls import path
from . import views

app_name='course_lesson'

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('course/<int:course_queue>/', views.course, name='course'),
    path('course/<int:course_queue>/module/<int:module_queue>/lesson/<int:lesson_queue>/',
         views.lesson, name='lesson'),
    path('course/<int:course_id>/course_end/', views.course_end, name='course_end'),


]