from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from . import forms
from .models import Tweet
# Create your views here.

def globalFeed(request):
    tweets = Tweet.objects.all()
    
    return render(request, 'globalFeed.html',{
            'form': forms.postTweet,
            'tweets': tweets
    })

def postTweet(request):
    if request.method == 'GET':
        return render(request, 'globalFeed.html',{
            'form': forms.postTweet
        })
    else:
        Tweet.objects.create(user = request.user, content = request.POST['content'])
        return redirect('/')

def like(request, id):
    tweet = Tweet.objects.get(id = id)
    user = request.user
    if user not in tweet.likes_users.all():
        tweet.likes += 1
        tweet.likes_users.add(user)
        tweet.save()
    else:
        tweet.likes -= 1
        tweet.likes_users.remove(user)
        tweet.save()
    
    return redirect('/')

def deleteTweet(request, id):
    tweet = Tweet.objects.get(id = id)
    tweet.delete()
    return redirect('/')

def responseTweet(request, id):
    if request.method == "POST":
        Tweet.objects.create(user = request.user, content = request.POST['contentResponse'], parent_tweet = id)
        return redirect('/')