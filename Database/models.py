from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime
from multiselectfield import MultiSelectField
import os
from django.conf import settings

def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.user.username, filename)

def file_upload_path(instance, filename):
    return '{0}/{1}/{2}'.format(instance.user.username, instance.project.projectName, filename)

class UserInformation(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    name = models.CharField(default="None", max_length=200)
    biography = models.TextField(default="None",)
    profilePicture = models.FileField(default='../media/defaultProfilePic.png',upload_to=user_directory_path,)

    skills = (
        ('C', 'C'),
        ('C++', 'C++'),
        ('JAVA', 'JAVA'),
        ('PYTHON', 'PYTHON'),
        ('RUBY','RUBY'),
        ('C#', 'C#'),
        ('FORTRAN', 'FORTRAN'),
        ('JAVASCRIPT', 'JAVASCRIPT'),
        ('HTML','HTML'),
        ('CSS','CSS'),
        ('PHP', 'PHP'),
    )
    skilltag = MultiSelectField(default='NONE',max_length=200, choices=skills)

    def __str__(self):
        return self.name

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projectName=models.CharField(max_length=250,blank=False)
    projectDescription = models.TextField(blank=False)
    accessType = models.CharField(default="Public" , max_length=25)
    projectCreatedAt = models.DateTimeField(default=datetime.now, blank=True)
    skills = (
        ('C', 'C'),
        ('C++', 'C++'),
        ('JAVA', 'JAVA'),
        ('PYTHON', 'PYTHON'),
        ('RUBY', 'RUBY'),
        ('C#', 'C#'),
        ('FORTRAN', 'FORTRAN'),
        ('JAVASCRIPT', 'JAVASCRIPT'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('PHP', 'PHP'),
    )
    skilltag = MultiSelectField(default='NONE', max_length=200, choices=skills,blank=True)




    def __str__(self):
        return self.projectName

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    uploader = models.CharField(max_length=200)
    file = models.FileField(upload_to=file_upload_path, )
    fileName = models.CharField(max_length=200)
    fileDescription = models.TextField(blank=True)
    fileSize = models.IntegerField()

    fileType = models.CharField(max_length=15)
    modificationTime = models.DateTimeField(default=datetime.now, blank=True)

    def relative_path(self):
        return os.path.relpath(self.path, settings.MEDIA_ROOT)

    def __str__(self):
        return str(self.file)

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    todo_description= models.TextField(blank=True)

class InProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    fileNames = models.TextField(blank=True)
    inProgress_description = models.TextField(blank=True)

class Done(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    fileNames = models.TextField(blank=True)
    done_description = models.TextField(blank=True)

class Version(models.Model):
    file=models.ForeignKey(File,on_delete=models.CASCADE)
    fileContent=models.TextField(default="First File")
    versionDescription = models.TextField(blank=True)
    versionFilename = models.CharField(max_length=200)
    versionFileSize = models.IntegerField()
    versionModificationTime =  models.DateTimeField(default=datetime.now, blank=True)

class AssignDeveloper(models.Model):
    project= models.ForeignKey(Project)
    assignDeveloper=models.ForeignKey(User)

class Comment(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    commentator=models.CharField(max_length=200)
    commentDescription=models.TextField(blank=True)

    commentTime=models.DateTimeField(default=datetime.now, blank=True)

class Issue(models.Model):
    issueCreator = models.ForeignKey(User, on_delete=models.CASCADE)
    project  = models.ForeignKey(Project, on_delete=models.CASCADE)
    fileName = models.CharField(max_length=200)
    label = models.CharField(max_length=100, default="Help Wanted")
    issueDescription = models.TextField()
    isClosed = models.BooleanField(default=False)
    issueTime = models.DateTimeField(default=datetime.now)

class Notification(models.Model):
    reciever = models.ForeignKey(User, on_delete=models.CASCADE)
    isViewed = models.BooleanField(default=False)
    content = models.TextField()
    link = models.URLField(blank=False)
    sender = models.CharField(max_length=200)
