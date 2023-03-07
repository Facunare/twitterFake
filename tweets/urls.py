from django.urls import path, include
from . import views

urlpatterns = [

    path('/globalFeed', views.globalFeed, name='globalFeed'),

]