from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, render_to_response, redirect
import Database
import os
import shutil
from django.conf import settings


class Search(object):
    def userIsAuthenticated(self, user):
        return user.is_authenticated

    def search(self,request):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return HttpResponse('You need to login')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        projects = Database.models.Project.objects.filter(user=user).order_by('-projectCreatedAt')


        if(request.method=='POST'):
            searchInput=request.POST['searchinput']


        else:
            searchInput=''


        numberOfUsers=Database.models.User.objects.filter(username=searchInput)
        numberofProjects = Database.models.Project.objects.filter(projectName=searchInput)


        if(numberOfUsers.count()>0):
            searchedUser=numberOfUsers[0]
            searchedUserProjects = Database.models.Project.objects.filter(user=searchedUser).order_by('-projectCreatedAt')
            isSame= False

            if(user==searchedUser):
                isSame = True

            if(isSame==False):

                context = {'userInformation': userInformation, 'user': user, 'projects': projects,
                       'searchedUser': searchedUser, 'searchedUserProjects':searchedUserProjects, 'isSame': isSame}
                return render(request, 'Search/searchedUser.html/', context)

            else:
                return redirect('/projectmanagement/')


        elif(numberofProjects.count()>0):
            allProjects = numberofProjects
            context = {'userInformation': userInformation, 'user': user, 'allProjects': allProjects}
            return render(request, 'Search/searchedAllProjectsShow.html', context)





    def searchedProjectDetails(self, request, username, projectname):

        user = request.user
        if (not self.userIsAuthenticated(user)):
            return HttpResponse('You need to login')
        userInformation = Database.models.UserInformation.objects.get(user=user)


        searchedUser = Database.models.User.objects.get(username=username)
        searchedProject = Database.models.Project.objects.get(user=searchedUser, projectName=projectname)

        files = Database.models.File.objects.filter(user=searchedUser, project=searchedProject)
        isSame = False

        if (user == searchedUser):
            isSame = True

        if (isSame == False):

            context = {'userInformation': userInformation, 'user': user, 'searchedUser': searchedUser,
                       'searchedProject': searchedProject, 'files': files, }

            return render(request, 'Search/searchedUserProjectDetails.html/', context)

        else:

            return redirect('/projectmanagement/'+searchedProject.projectName+'/')



    def readFile(self, fileUrl):
        f = open(fileUrl, 'r')
        return f.readlines()


    def replaceNewLine(self, linesFile):
        lineWdoutSPNL = []

        for i in range(len(linesFile)):
            tempLine = linesFile[i].replace('\n', '').replace('\t', "    ")
            lineWdoutSPNL.append(tempLine)

        return lineWdoutSPNL

    def searchedFileDetails(self, request, username, projectname, id):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return HttpResponse('You need to login')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        file = Database.models.File.objects.get(pk=id)

        fileUrl = file.file.path
        linesInFile = self.replaceNewLine(self.readFile(fileUrl))
        numberOfLines = len(linesInFile)

        context = {'lines': linesInFile, 'file': file, 'userInformation': userInformation, 'user': user,
                        'numberOfLines': numberOfLines}

        return render(request, 'Search/searchedFileDetails.html', context)

    def createZipFile(self, username, projectName):
        zippath = os.path.join(settings.BASE_DIR, 'media', username, projectName, 'download')
        directoryOfFiles = os.path.join(settings.BASE_DIR, 'media', username, projectName)
        shutil.make_archive(zippath, 'zip', directoryOfFiles)

    def openZipFile(self, username, projectName):
        return open(os.path.join(settings.BASE_DIR, 'media', username, projectName, 'download.zip'), 'rb')


    def downloadFiles(self, request, username, projectname):

        user = request.user

        if (not self.userIsAuthenticated(user)):
            return HttpResponse('You need to login')

        searchedUser = Database.models.User.objects.get(username=username)
        searchedProject = Database.models.Project.objects.get(user=searchedUser, projectName=projectname)

        self.createZipFile(searchedUser.username, searchedProject.projectName)

        zip_file = self.openZipFile(searchedUser.username, searchedProject.projectName)

        response = HttpResponse(zip_file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="%s"' % 'download.zip'
        return response
