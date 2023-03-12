from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.globalFeed, name='globalFeed'),
    path('post/', views.postTweet, name="postTweet"),
    path('post/response/<int:id>', views.responseTweet, name="responseTweet"),
    path('like/<int:id>', views.like, name="like"),
    path('like/<int:id>/delete', views.deleteTweet, name="deleteTweet"),
    
]