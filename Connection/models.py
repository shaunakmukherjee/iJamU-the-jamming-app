#Connection/models.py

from django.db import models

# Create your models here.
class Connection(models.Model):
    User1 = models.CharField(max_length=50)
    User2 = models.CharField(max_length=50)
    Endorsed = models.BooleanField(default = "False")

    def __str__(self):
        return str(self.User1)

class Crequest(models.Model):
    User1 = models.CharField(max_length=50)
    User2 = models.CharField(max_length=50)
    Endorsed = models.BooleanField(default = "False")

    def __str__(self):
        return str(self.User2)