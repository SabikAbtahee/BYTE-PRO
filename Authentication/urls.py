from django.conf.urls import url


from . import views
urlpatterns = [




    url('signin/', views.Authentication().signIn, name='signIn'),
    url('signup/', views.Authentication().signUp, name='signUp'),
    url('recovery/', views.Authentication().recovery, name='recovery'),
]