from django.db import models


# Create your models here.
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, default="")
    body = models.TextField(default="")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, default="")
    email = models.EmailField(max_length=32, default="")
    password = models.CharField(max_length=32, default="", null=True, blank=True)
