from django.contrib import admin
from .models import UserInformation ,Project, ProjectTag, File, Version
# Register your models here.
admin.site.register(UserInformation)
admin.site.register(Project)
admin.site.register(File)
admin.site.register(ProjectTag)
admin.site.register(Version)
