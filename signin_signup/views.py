from django.shortcuts import render, render_to_response
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf


# Create your views here.


def sign_in(request):
    return render(request, 'signin_signup/sign_in.html')


def sign_up(request):
    return render(request, 'signin_signup/sign_up.html')

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


