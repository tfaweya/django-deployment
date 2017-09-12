from django.db import models
from django.contrib.auth.models import User

class TestUser(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)

    def __str__(self):
        return self.first_name



class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    portfolio_site = models.URLField(blank=True)
    profile_pic = model.ImageField(upload_to='profilepics', blank = True)


    def __str__(self):
        return self.user.username
