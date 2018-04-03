from django.conf.urls import url


from . import views
urlpatterns = [




    url('signin/', views.Authentication().signIn, name='signIn'),
    url('signup/', views.Authentication().signUp, name='signUp'),
    url('recovery/', views.Authentication().recovery, name='recovery'),
<<<<<<< HEAD
    url('adduser/', views.Authentication().adduser, name='adduser'),
=======
>>>>>>> af2b13902b8da9bf936dd179aa15958befa19449
]