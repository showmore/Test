from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

    def __str__(self):
        return self.user


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    QQ = models.CharField(max_length=128, blank=True)
    blog = models.CharField(max_length=128, blank=True)
    location = models.CharField(max_length=128, blank=True)
    occupation = models.CharField(max_length=64, blank=True)

    reward = models.IntegerField(default=0, blank=True)
    topic_count = models.IntegerField(default=0, blank=True)
    post_count = models.IntegerField(default=0, blank=True)
