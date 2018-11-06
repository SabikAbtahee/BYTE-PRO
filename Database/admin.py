from django.contrib import admin
from .models import UserInformation ,Project,  File, Version, Notification, AssignDeveloper, Issue
# Register your models here.
admin.site.register(UserInformation)
admin.site.register(Project)
admin.site.register(File)
admin.site.register(Notification)
admin.site.register(Version)
admin.site.register(AssignDeveloper)
admin.site.register(Issue)