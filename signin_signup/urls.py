
from django.urls import path
from . import views

app_name='signin_signup'

urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),

]


# urlpatterns = [
#     path('', views.index, name='index'),
#     path('login/', views.login1, name='login'),
#     path('check/', views.check, name='check')
# ]

