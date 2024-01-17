from django.db import models


# Create your models here.
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, default="")
    body = models.TextField(default="")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
