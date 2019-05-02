from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url=reverse_lazy('signin_signup:sign_in'))
def profile(request):
    user = request.user
    content = {}
    content['user'] = user
    return render(request, 'user_profile/profile.html', content)
