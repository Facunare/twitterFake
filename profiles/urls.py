from django.urls import path, include
from . import views

urlpatterns = [


    path('/<str:account>', views.myProfile, name="myProfile")   
]