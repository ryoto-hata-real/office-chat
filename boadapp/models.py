from django.db import models

class BoardModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=50)
    images = models.ImageField(upload_to='', blank=True)
    good = models.IntegerField(default=0)
    read = models.IntegerField(default=0)
    readtext = models.CharField(max_length=200,blank=True)
