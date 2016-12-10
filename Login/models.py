from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userdetail(models.Model):
    Username = models.ForeignKey(User,unique=True)
    Fname = models.CharField(max_length=25)
    Lname = models.CharField(max_length=25)
    Nickname=models.CharField(max_length=25)
    Techlevel=models.DecimalField(max_digits=1,decimal_places=0,default=1)
    Year=models.DecimalField(max_digits=2,decimal_places=0)
    Rating=models.DecimalField(max_digits=1,decimal_places=0)
    Bio=models.TextField(max_length=300,blank=True)
    Genre=models.TextField(max_length=300,blank=True)
    Address=models.TextField(max_length=300)
    Instruments=models.TextField(max_length=300,blank=True)

  

    def __str__(self):
        return str(self.Username)


class Search(models.Model):
    Criteria = models.CharField(max_length=200)
    

    def __str__(self):
        return self.Criteria



class Connection(models.Model):
    User1 = models.CharField(max_length=50)
    User2 = models.CharField(max_length=50)
    Endorsed = models.BooleanField(default = "False")

    def __str__(self):
        return self.User1

class Crequest(models.Model):
    User1 = models.CharField(max_length=50)
    User2 = models.CharField(max_length=50)
    Endorsed = models.BooleanField(default = "False")

    def __str__(self):
        return self.User1