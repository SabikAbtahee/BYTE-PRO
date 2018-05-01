from django.conf.urls import url, include
# ----------------Default Authentication------------------
from django.contrib import admin
from django.contrib.auth import views as auth_views
# ------------------          *****         --------------


from . import views

urlpatterns = [

    url(r'^signup/', views.Authentication().signUp, name='signUp2'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.Authentication().activate, name='activate'),
    url(r'^signin', auth_views.login, name = "login"),
     # url(r'^logout', auth_views.logout, name = "logout"),
    url(r'^logout', views.Authentication().logout, name = "logout"),

    
   	url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        views.PasswordResetConfirmView.as_view(), name='reset_password_confirm'),
    url(r'^reset_password',
        views.ResetPasswordRequestView.as_view() , name='reset_password'),

    # ----------------
    # url(r'^home/', views.Authentication().index, name = "index"),
    url(r'^home/',include('Project.urls')),
	# ----------------
	


]