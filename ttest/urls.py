
from django.urls import path
from . import views

app_name='test'

urlpatterns = [
    path('test/', views.test, name='test'),
    path('test_result/', views.test_result, name='test_result'),
]


# urlpatterns = [
#     path('', views.test),
#     path('result/', views.test_result)
# ]
