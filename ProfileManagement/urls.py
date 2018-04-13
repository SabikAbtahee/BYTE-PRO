from django.conf.urls import url
from django.contrib import admin

from django.views.generic.base import TemplateView

from django.conf.urls import include
from django.conf import settings
from django.views.static import serve

from . import views
urlpatterns = [

    url(r'', views.ProfileManagement().profileView  , name="profileView"),

]