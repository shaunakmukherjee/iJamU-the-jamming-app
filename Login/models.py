from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userdetail(models.Model):
    Username = models.ForeignKey(User,unique=True)
    Fname = models.CharField(max_length=25)
    Lname = models.CharField(max_length=25)
    Nickname=models.CharField(max_length=25)
    Techlevel=models.DecimalField(max_digits=1,decimal_places=0)
    Year=models.DecimalField(max_digits=2,decimal_places=0)
    Rating=models.DecimalField(max_digits=1,decimal_places=0)
    Bio=models.TextField(max_length=300)
    Genre=models.TextField(max_length=300)
    Address=models.TextField(max_length=300)
    Instruments=models.TextField(max_length=300)

  

    def __str__(self):
        return str(self.Username)


class Search(models.Model):
    Criteria = models.CharField(max_length=200)
    

    def __str__(self):
        return self.Criteria



class Connection(models.Model):
    User1 = models.CharField(max_length=50)
    User2 = models.ForeignKey(Userdetail,to_field='Username')
    Endorsed = models.BooleanField(default = "False")

    def __str__(self):
        return self.User1

class Request(models.Model):
    User1 = models.CharField(max_length=50)
    User2 = models.ForeignKey(Userdetail,to_field='Username')
    Endorsed = models.BooleanField(default = "False")

    def __str__(self):
        return self.User1