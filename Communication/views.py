from django.http import HttpResponse
from django.shortcuts import render, redirect
import Database
from django.contrib.auth.models import User
# Create your views here.
class Communication(object):
    def userIsAuthenticated(self, user):
        return user.is_authenticated

    def returnAllUserANdProjects(self):
        allprojects = Database.models.Project.objects.all()
        alluser = Database.models.User.objects.all()
        return alluser, allprojects

    def assignDevelopers(self,request, projectname):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return HttpResponse('You need to login')
        userInformation = Database.models.UserInformation.objects.get(user=user)

        project = Database.models.Project.objects.get(user=user, projectName = projectname)

        if(request.method=='POST'):

            assignedDevForm = request.POST['assignDeveloper'] #getting inputs from form

            if(len(assignedDevForm.replace(' ',''))!=0):

                numberOfAssignedDev = User.objects.filter(username=assignedDevForm) #getting all the query set for that assigned developer [as user]

                if(numberOfAssignedDev.count()!=0): # if that assigned developer is actually exist as user
                    assignedDev = numberOfAssignedDev[0] # getting the first value

                    if(Database.models.AssignDeveloper.objects.filter(project = project, assignDeveloper = assignedDev).count()==0 and user!=assignedDev): #if the user assigned before and the owner is not the assigned
                        AssignDevelopers = Database.models.AssignDeveloper(project = project, assignDeveloper = assignedDev)
                        AssignDevelopers.save()
            #may have {else} condition to show user whats the wrong.



        return redirect('/projectmanagement/'+project.projectName+'/')