from django.contrib import admin
from .models import UserInformation ,Project, ProjectTag
# Register your models here.
admin.site.register(UserInformation)

admin.site.register(Project)
admin.site.register(ProjectTag)

