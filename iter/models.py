from django.db import models
from django.utils import timezone

TECH_LEVEL_CHOICES = (
    ("1", '1'),
    ("2", '2'),
    ("3", '3'),
    ("4", '4'),
    ("5", '5'),
)

INSTRUMENT_CHOICE = (
    ("None",'None'),
    ("Drums",'Drums'),
    ("Guitar",'Guitar'),
)

class Userdetails(models.Model):
    Username = models.CharField(max_length=50)
    Fname = models.CharField(max_length=25)
    Lname = models.CharField(max_length=25)
    Nickname=models.CharField(max_length=25)
    Techlevel=models.CharField(max_length=1,choices=TECH_LEVEL_CHOICES,default='1')
    Year=models.DecimalField(max_digits=2,decimal_places=0)
    Rating=models.DecimalField(max_digits=1,decimal_places=0)
    Bio=models.TextField(max_length=300)
    Genre=models.TextField(max_length=300,default="Electric")
    Instruments=models.TextField(max_length=300,default="Drums")

  

    def __str__(self):
        return self.Username



class Search(models.Model):
    Genre = models.CharField(max_length=200)
    Instruments = models.CharField(max_length=200,choices=INSTRUMENT_CHOICE,default='None')

    def __str__(self):
        return self.Instruments

class Connections(models.Model):
    User1 = models.CharField(max_length=50)
    User2 = models.CharField(max_length=50)

    def __str__(self):
        return self.User1
