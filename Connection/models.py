#Connection/models.py

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Connection(models.Model):
    User1 = models.CharField(max_length=50)
    User2 = models.CharField(max_length=50)
    Endorsed = models.BooleanField(default = "False")

    def __str__(self):
        return str(self.User2)

class Crequest(models.Model):
    User1 = models.CharField(max_length=50)
    User2 = models.CharField(max_length=50)
    Endorsed = models.BooleanField(default = "False")

    def __str__(self):
        return str(self.User2)

class Endorsement(models.Model):
    User1 = models.CharField(max_length=50)
    User2 = models.CharField(max_length=50)
    Endorsed = models.BooleanField(default = "True")
	
    def _str_(self):
	    return str(self.User2)

class Endorsedetails(models.Model):
    Username = models.ForeignKey(User,unique=True)
    Nickname=models.CharField(max_length=25)
    Techlevel=models.DecimalField(max_digits=1,decimal_places=0,default=1)
    Rating=models.DecimalField(max_digits=1,decimal_places=0)
    Comments=models.TextField(max_length=300,blank=True)
    

    def __str__(self):
        return str(self.Username)
