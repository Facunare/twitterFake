from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from . import forms
from .models import Tweet
# Create your views here.

# 1. Landing page for unlogined people
# 2. Profiles
# 3. Followage and try messenger.
# 4. Retweet
# 5. Trends
# 6. Gmail login
# 7. Function for the post of tweets. (add images, emojis, self location, pools)
# 8. Share tweet
# 9. Create modals (especially for responses)
# 10. Keep tweets. ("guardados section")
# 11. Settings section
# 12. Admin view (Data analytics, moderate content (ban and delete accounts and tweets that are breaking the rules ))
# 13. Design 

def globalFeed(request):
    tweets = Tweet.objects.all().filter(parent_tweet = None)
    
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
    
def tweetDetails(request, id):
    responses = Tweet.objects.all().filter(parent_tweet = id)
    return render(request, 'tweetDetail.html',{
        'responses': responses
    })
    
def searchTweet(request):
    search = request.GET.get("search")
    
    if search:
        tweets = Tweet.objects.filter(content__icontains = search)
        
    return render(request, 'globalFeed.html',{
        'tweets': tweets
    })