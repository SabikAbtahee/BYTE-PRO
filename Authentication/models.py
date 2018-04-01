from django.db import models

# Create your models here.
from datetime import datetime

def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.name, filename)

class User(models.Model):
    name = models.CharField(max_length=200)
    userName = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email=models.EmailField()
    biography = models.TextField()
    profilePicture = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.name + "-" + self.email

class SkillTag(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    skilltag=models.CharField(max_length=20)