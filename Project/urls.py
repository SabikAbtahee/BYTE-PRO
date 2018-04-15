from django.conf.urls import url, include

from django.contrib import admin
from django.contrib.auth import views as auth_views



from . import views

urlpatterns = [



    url(r'^$', views.Project().homePage, name="homepage" ),
    url(r'^addproject/', views.Project().addProject, name='addProject'),

    url(r'^(?P<projectname>[\w\-]+)/(?P<id>[0-9]+)/',views.Project().fileDetails, name = 'fileDetails'),
    url(r'^(?P<projectname>[\w\-]+)/addfiles/',views.Project().addFile, name = 'addFile'),
    # here can be change[we can use project name or project id.]
    url(r'^(?P<projectname>[\w\-]+)/',views.Project().projectDetails, name = 'projectDetails'),
]