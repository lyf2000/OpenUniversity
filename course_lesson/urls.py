from django.urls import path
from . import views

app_name='course_lesson'

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('course/<int:course_id>/', views.course, name='course'),
    path('course/<int:course_id>/module/<int:module_id>/lesson/<int:lesson_id>/',
         views.lesson, name='lesson'),
    path('course/<int:course_id>/course_end/', views.course_end, name='course_end'),

]