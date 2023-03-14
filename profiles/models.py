from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profiles(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE )
    username = models.CharField(max_length=30, null=True)
    biography = models.TextField(max_length=250,  null=True)
    profileImage = models.ImageField(null=True)
    followers = models.IntegerField(default=0)
    followers_users = models.ManyToManyField(User, related_name="followers_users", null=True)
    birthday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
