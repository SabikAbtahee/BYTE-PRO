from django.shortcuts import render
from django.views.generic import TemplateView
<<<<<<< HEAD
from django.http import HttpResponse
# Create your views here.
import Database
=======
# Create your views here.

>>>>>>> af2b13902b8da9bf936dd179aa15958befa19449
class Authentication(object):

    def signIn(self, request):
        return render(request,'Authentication/signIn.html')

    def signUp(self, request):
        return render(request, 'Authentication/signUp.html')

    def recovery(self,request):
<<<<<<< HEAD
        return render(request, 'Authentication/recovery.html')

    def adduser(self,request):
    	if(request.method=="POST"):
    		# request.POST.get('is_private', False)
            name = request.POST.get("name", False)
            username = request.POST.get('username', False)
            password = request.POST.get("password", False)
            email=request.POST.get("email", False)
            confirmPassword=request.POST.get("confirmPassword", False)

            user1=Database.models.UsersAll(name=name,userName=username,password=password,email=email)
            user1.save()

            return HttpResponse("YA MAN")

    		
=======
        return render(request, 'Authentication/recovery.html')
>>>>>>> af2b13902b8da9bf936dd179aa15958befa19449
