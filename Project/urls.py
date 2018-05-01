from django.conf.urls import url, include

from django.contrib import admin
from django.contrib.auth import views as auth_views



from . import views

urlpatterns = [



    url(r'^$', views.Project().homePage, name="homepage" ),

    url(r'^addproject/$', views.Project().addProject, name='addProject'),
    url(r'^(?P<projectname>[\w\-]+)/(?P<id>[0-9]+)/comparewithprevious/$', views.Project().compareWithPreviousVersion,
        name='compareWithPreviousVersion'),
    url(r'^(?P<projectname>[\w\-]+)/(?P<id>[0-9]+)/edit/$', views.Project().editFile, name='editFile'),
    url(r'^(?P<projectname>[\w\-]+)/(?P<id>[0-9]+)/versions/$', views.Project().showVersions, name='showVersions'),

    url(r'^(?P<projectname>[\w\-]+)/(?P<id>[0-9]+)/$',views.Project().fileDetails, name = 'fileDetails'),

    url(r'^(?P<projectname>[\w\-]+)/projectsettings/$',views.Project().projectSettings, name = 'projectSettings'),

    url(r'^(?P<projectname>[\w\-]+)/downloadfiles/$',views.Project().downloadFiles, name = 'downloadFiles'),
    url(r'^(?P<projectname>[\w\-]+)/(?P<fid>[0-9]+)/(?P<vid>[0-9]+)/rebase/$',views.Project().rebaseFile, name = 'rebaseFile'),

    url(r'^(?P<projectname>[\w\-]+)/addfiles/$', views.Project().addFile, name='addFile'),
    # here can be change[we can use project name or project id.]
    url(r'^(?P<projectname>[\w\-]+)/$',views.Project().projectDetails, name = 'projectDetails'),

    url(r'^(?P<projectname>[\w\-]+)/(?P<aid>[0-9]+)/deletedeveloper/$',views.Project().deleteDeveloper, name = 'deleteDeveloper'),

    url(r'^(?P<projectname>[\w\-]+)/(?P<id>[0-9]+)/deletefile/$',views.Project().deleteFile, name = 'deleteFile'),
    url(r'^(?P<projectname>[\w\-]+)/projectProgress/$',views.Project().projectProgress, name = 'projectProgress'),







    # here can be change[we can use project name or project id.]


]