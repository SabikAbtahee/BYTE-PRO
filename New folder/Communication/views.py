from django.http import HttpResponse, JsonResponse
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
    #
    # reciever = models.ForeignKey(User, on_delete=models.CASCADE)
    # isViewed = models.BooleanField(default=False)
    # content = models.TextField()
    # link = models.URLField(blank=False)
    # sender = models.CharField(max_length=200)
    def addToNotificationTable(self, sender, reciever, projectname, type, fileNumbers, fileName, isMaster):
        content = None
        link = None
        _url_target = None
        if(isMaster):
            _url_target = sender
        else:
            _url_target = reciever.username

        if(type =="assign"):
            content = sender + " assigned you in project: "+projectname +"."
            link = "/search"+"/"+_url_target+"/"+projectname+"/"
        elif(type=="upload"):
            content = sender + " uploaded " + str(fileNumbers) + "files in project:"+ projectname+"."
            link = "/search"+"/"+_url_target+"/"+projectname+"/"
        elif(type=="comment"):
            content = sender + " commented in " + fileName + " in " + projectname+"."
            link = "/search" + "/" + _url_target + "/" + projectname + "/" + fileName + "/"
        elif(type == "issue"):
            content = sender + " created issue in " +  projectname+"."
            link = "/search" + "/" + _url_target + "/" + projectname + "/issues/"
        Notification =  Database.models.Notification(reciever = reciever, isViewed = False, content = content, link = link, sender = sender )
        Notification.save()



    def queryAsList(self, noti):
        listNoti = []
        for n in noti:
            listNoti.append(n.reciever.username)
            listNoti.append(n.isViewed)
            listNoti.append(n.content)
            listNoti.append(n.link)
            listNoti.append(n.sender)
            User = Database.models.User.objects.get(username = n.sender)
            propic = Database.models.UserInformation.objects.get(user=User).profilePicture.url
            listNoti.append(propic)
        return  listNoti


    def getNotifications(self,request):
        id = request.GET.get('uid', None)
        User = Database.models.User.objects.get(pk=id)
        noti = Database.models.Notification.objects.filter(reciever = User).order_by('-id')
        listNotification  = self.queryAsList(noti)
        data = {
            'num': noti.count(),
            'content': listNotification

        }
        return JsonResponse(data, safe = False)

    def notifiedAllAssignedDevelopers(self, project, sender, fileNumbers, isMaster, type):
        if(type=="comment"):
            AssignDev = Database.models.AssignDeveloper.objects.filter(project=project)
            tempUser = Database.models.User.objects.get(username=sender)
            for assignDev in AssignDev:
                if (assignDev.assignDeveloper.username != tempUser.username):
                    self.addToNotificationTable(sender, assignDev.assignDeveloper, project.projectName, type,
                                                fileNumbers, str(fileNumbers), isMaster)
                    print("called for loop")
            print(str(fileNumbers))
            if (isMaster == False):
                self.addToNotificationTable(sender, project.user, project.projectName, type, fileNumbers, str(fileNumbers), isMaster)
                print("called ifelse")
        else:
            AssignDev = Database.models.AssignDeveloper.objects.filter(project=project)
            tempUser = Database.models.User.objects.get(username=sender)
            for assignDev in AssignDev:
                if (assignDev.assignDeveloper.username != tempUser.username):
                    self.addToNotificationTable(sender, assignDev.assignDeveloper, project.projectName, type,
                                                fileNumbers, "", isMaster)
                    print("called for loop")
            if (isMaster == False):
                self.addToNotificationTable(sender, project.user, project.projectName, type, fileNumbers, "", isMaster)
                print("called ifelse")




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
                        self.addToNotificationTable(request.user.username, assignedDev, projectname, "assign", None, None, True)
            #may have {else} condition to show user whats the wrong.



        return redirect('/projectmanagement/'+project.projectName+'/')

    def fetchImage(self, request):
        print("called")
        id = request.GET.get('pid', None)
        project = Database.models.Project.objects.get(pk=id)
        files = Database.models.File.objects.filter(project=project).order_by('-id')
        print(files)
        propics = []
        data = {}
        for file in files:
            user = Database.models.User.objects.get(username = file.uploader)
            userInformation = Database.models.UserInformation.objects.get(user=user)
            data[file.id] = userInformation.profilePicture.url
            # print(userInformation.profilePicture.url)
        data['success'] = True
        return JsonResponse(data, safe=False)

