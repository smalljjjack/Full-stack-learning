from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length = 264, unique = True)

    def __str__(self):
        return self.top_name;

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length = 264, unique = True)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return self.date
'''
class User(models.Model):
    FName = models.CharField(max_length = 264)
    LName = models.CharField(max_length = 264)
    Email = models.CharField(max_length = 264)

    def __str__(self):
        return self.FName + self.LName
'''

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)

    # additional
    portfolio_site = models.URLField(blank = True)

    profile_pic = models.ImageField(upload_to = 'profile_pics',blank = True)

    def __str__(self):
        return self.user.username
