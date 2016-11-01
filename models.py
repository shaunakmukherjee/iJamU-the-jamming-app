from django.db import models

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    class Meta:
        ordering = ('created',)

class Snippet1(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    nickname = models.CharField(max_length=20)
    techlevel = models.IntegerField()
    years = models.IntegerField()
    rating = models.IntegerField()
    bio= models.CharField(max_length=200)

    class Meta:
        ordering = ('created',)

class Snippet2(models.Model):
	username = models.CharField(max_length=50)
	instrument = models.CharField(max_length=20)
	genre = models.CharField(max_length=20)

#    class Meta:
#        ordering = ('created',)
