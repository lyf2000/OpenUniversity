from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .forms import *

# Create your views here.


def sign_in(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user_profile:profile"))

    content = {}
    content.update(csrf(request))
    form = LoginForm(request.POST or None)
    content['form'] = form
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("user_profile:profile"))
        else:
            error_message = "Такого пользователя нет"
            content['error_message'] = error_message
            return render(request, 'signin_signup/sign_in.html', content)

    return render(request, 'signin_signup/sign_in.html', content)


def sign_up(request):
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('succes_signup'))
    return render(request, 'signin_signup/sign_up.html', args)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("pages:index"))

def check(request):
    return render(request, 'signin_signup/check.html')


# def login1(request):
# 	if request.user.is_authenticated:
# 		return render(request, 'signin_signup/check.html')
# 	else:
# 		args = {}
# 		args.update(csrf(request))
# 		if request.POST:
# 			username = request.POST.get('email', '')
# 			password = request.POST.get('password', '')
# 			user = auth.authenticate(username=username, password=password)
# 			if user is not None:
# 				auth.login(request, user)
# 				return HttpResponseRedirect(reverse('check'))
# 			else:
# 				args['login_error'] = "User is not found"
# 				return render_to_response('signin_signup/sign_in.html', args)
# 		else:
# 			return render_to_response('signin_signup/sign_in.html', args)
#

