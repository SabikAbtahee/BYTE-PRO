"""SPL2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from django.views.generic.base import TemplateView

from django.conf.urls import include
from django.conf import settings
from django.views.static import serve
import ProfileManagement, Project, Communication, Authentication


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^authentication/', include('Authentication.urls')),
    url(r'^profilemanagement/', include('ProfileManagement.urls')),
    url(r'^projectmanagement/', include('Project.urls')),

    url(r'^ajax/passwordCheck/$', ProfileManagement.views.ProfileManagement().passwordCheck , name="passwordCheck"),
    url(r'^ajax/projectExists/$', Project.views.Project().projectCheck , name="projectCheck"),

    url(r'^pro/ajx/close/$', Project.views.Project().closeIssue, name="closeIssue"),
    url(r'^ajax/getnotifications$', Communication.views.Communication().getNotifications, name="getNotifications"),
    url(r'^comm/ajx/fetchimg/$', Communication.views.Communication().fetchImage, name="fetchImage"),
    url(r'^search/', include('Search.urls')),
    url(r'^comm/', include('Communication.urls')),
    url(r'^ajax/checkemail/$', Authentication.views.Authentication().checkEmail, name="checkEmail"),
    url(r'^project/fetchlanguagedata/$', Project.views.Project().fetchLanguage, name="fetchLanguage"),


]

if(settings.DEBUG):
    urlpatterns+=[url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT,}),]


