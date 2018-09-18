from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Logininfo(models.Model):
    first_name=models.CharField(max_length=250,unique=True)
    last_name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    objects=models.Manager()
    def __str__(self):
        return self.first_name

#class for autho=enticsting 
class userprofileinfo(models.Model):
    user=models.OneToOneField(User)
    portfolio_user=models.URLField(blank=True,null=True)
    profile_image=models.ImageField(upload_to='profile_pics',blank=True,null=True)
    objects=models.Manager()
    def __str__(self):
        return self.user.username
    