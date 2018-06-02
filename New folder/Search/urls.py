
from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [

    url(r'^ajx/merge/$',views.Search().merge, name = 'merge'),
    url(r'^(?P<username>[\w\-]+)/(?P<projectname>[\w\-]+)/$', views.Search().searchedProjectDetails,
        name='searchedProjectDetails'),
    url(r'^(?P<username>[\w\-]+)/(?P<projectname>[\w\-]+)/(?P<id>[0-9]+)/$',views.Search().searchedFileDetails, name = 'searchedFileDetails'),
    url(r'^(?P<username>[\w\-]+)/(?P<projectname>[\w\-]+)/(?P<id>[0-9]+)/comparewithprevious',views.Search().compareWithPreviousVersion, name = 'compareWithPreviousVersion'),

    url(r'^(?P<username>[\w\-]+)/(?P<projectname>[\w\-]+)/(?P<id>[0-9]+)/issues', views.Search().fileIssue,
        name='fileIssue'),

    url(r'^(?P<username>[\w\-]+)/(?P<projectname>[\w\-]+)/(?P<id>[0-9]+)/versions$',views.Search().showVersions, name = 'showVersions'),
    url(r'^(?P<username>[\w\-]+)/(?P<projectname>[\w\-]+)/addfiles/$',views.Search().addFile, name = 'addFile'),

    url(r'^(?P<username>[\w\-]+)/(?P<projectname>[\w\-]+)/downloadfiles/$',views.Search().downloadFiles, name = 'downloadFiles'),
    url(r'^(?P<username>[\w\-]+)/(?P<projectname>[\w\-]+)/issues/$', views.Search().projectIssue, name='projectIssue'),
    url(r'^$', views.Search().search, name="search"),

    url(r'^(?P<username>[\w\-]+)/(?P<projectname>[\w\-]+)/(?P<id>[0-9]+)/comment/$',views.Search().commentOnFile, name = 'searchedComment'),



]




