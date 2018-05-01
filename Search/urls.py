
from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [

    url(r'^(?P<username>[\w\-]+)/(?P<projectname>[\w\-]+)/$', views.Search().searchedProjectDetails,
        name='searchedProjectDetails'),
    url(r'^(?P<username>[\w\-]+)/(?P<projectname>[\w\-]+)/(?P<id>[0-9]+)/$',views.Search().searchedFileDetails, name = 'searchedFileDetails'),
url(r'^(?P<username>[\w\-]+)/(?P<projectname>[\w\-]+)/downloadfiles/$',views.Search().downloadFiles, name = 'downloadFiles'),
    url(r'^$', views.Search().search, name="search"),



]




