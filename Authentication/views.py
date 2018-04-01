from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Authentication(object):

    def signIn(self, request):
        return render(request,'Authentication/signIn.html')

    def signUp(self, request):
        return render(request, 'Authentication/signUp.html')

    def recovery(self,request):
        return render(request, 'Authentication/recovery.html')