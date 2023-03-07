from django.shortcuts import render

# Create your views here.

def globalFeed(request):
    return render(request, 'globalFeed.html')