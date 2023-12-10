from django.db import models

# Create your models here.

class FileQueryAnswer(models.Model):
    fileId = models.IntegerField()
    query = models.CharField()
    answer = models.CharField()