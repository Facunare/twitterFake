from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def myProfile(request, account):
    user = User.objects.get(username = account)
    return render(request, 'myProfile.html', {
        'user': user
    })