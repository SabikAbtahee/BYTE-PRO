from django.shortcuts import render, redirect
from django.http import HttpResponse
import Database
from django.contrib.auth.models import User
from django.conf import settings
import os

import os, tempfile, zipfile, mimetypes
from wsgiref.util import FileWrapper
from django.conf import settings

class Project(object):
    def homePage(self, request):
        user = request.user
        userInformation = Database.models.UserInformation.objects.get(user=user)
        projects = Database.models.Project.objects.filter(user=user).order_by('-projectCreatedAt')
        context = {'userInformation': userInformation, 'user': user, 'projects': projects}
        return render(request, 'Project/home.html', context)

    def getProjectUrl(self, username, projectName):
        return '{0}/{1}/{2}/{3}'.format(settings.MEDIA_ROOT, username, 'Projects', projectName)

    def addProject(self, request):
        user = request.user
        userInformation = Database.models.UserInformation.objects.get(user=user)
        if (request.method == 'POST'):
            projectName = request.POST['projectName']
            projectDescription = request.POST['projectDescription']
            accessType = request.POST['accessType']
            project = Database.models.Project(user=user, projectName=projectName, projectDescription=projectDescription,
                                              accessType=accessType)
            project.save()

            projectUrl = self.getProjectUrl(user.username, projectName)
            if not os.path.exists(projectUrl):
                os.makedirs(projectUrl)
            return redirect('/projectmanagement/')
        else:
            context = {'userInformation': userInformation, 'user': user}
            return render(request, 'Project/addProject.html', context)

    def projectDetails(self, request, projectname):
        user = request.user
        userInformation = Database.models.UserInformation.objects.get(user=user)
        print(projectname)
        project = Database.models.Project.objects.get(projectName=projectname)
        files = Database.models.File.objects.filter(user=user, project=project).order_by('-modificationTime')
        context = {'userInformation': userInformation, 'user': user, 'project': project, 'files': files}
        return render(request, 'Project/projectDetails.html', context)

    def getFileNameAndType(self, fileName):
        typeOfFile = fileName.split('.')[1]
        fileNameWdOutExtention = fileName.split('.')[0]

        if (typeOfFile == 'cpp'):
            typeOfFile = 'C++'
        elif (typeOfFile == 'cs'):
            typeOfFile = 'C#'
        elif (typeOfFile == 'css'):
            typeOfFile = 'CSS'
        elif (typeOfFile == 'html' or typeOfFile == 'htm'):
            typeOfFile = 'html'
        elif (typeOfFile == 'java' or typeOfFile == 'jsp'):
            typeOfFile = 'Java'
        elif (typeOfFile == 'javascript' or typeOfFile == 'js' or typeOfFile == 'jsx'):
            typeOfFile = 'JavaScript'
        elif (typeOfFile == 'php' or typeOfFile == 'php3' or typeOfFile == 'php4' or typeOfFile == 'php5' or typeOfFile == 'php6'):
            typeOfFile = 'PHP'
        elif (typeOfFile == 'python' or typeOfFile == 'py'):
            typeOfFile = 'Python'
        return typeOfFile, fileNameWdOutExtention

    #-----------------------------------------------------FILE PURPOSE-------------------------------------------
    def addFile(self, request, projectname):
        user = request.user
        userInformation = Database.models.UserInformation.objects.get(user=user)
        project = Database.models.Project.objects.get(projectName=projectname)
        if (request.method == 'POST'):
            file = request.FILES['file']
            fileDescription = request.POST['fileDescription']
            fileName = file.name
            fileSize = file.size
            fileType, fileNameWdOutExtention = self.getFileNameAndType(fileName)


            x=Database.models.File.objects.filter(user=user,project=project,fileName=fileName)

            print(x.count())



            File = Database.models.File()

            File.user = user
            File.project = project
            File.file = file
            File.fileDescription = fileDescription
            File.fileName = fileName
            File.fileSize = fileSize
            File.fileType = fileType
            File.save()

            return redirect('/projectmanagement/' + project.projectName + '/')

        else:
            context = {'userInformation': userInformation, 'user': user, 'project': project}
            return render(request, 'Project/addFile.html', context)


    # def checkVersion(self):






    def readFile(self, fileUrl):
        f = open(fileUrl, 'r')
        return f.readlines()

    def replaceNewLine(self, linesFile):
        lineWdoutSPNL = []

        for i in range(len(linesFile)):
            tempLine = linesFile[i].replace('\n', '').replace('\t',"    ")
            lineWdoutSPNL.append(tempLine)

        return lineWdoutSPNL

    def fileDetails(self, request, projectname, id):
        user = request.user
        userInformation = Database.models.UserInformation.objects.get(user=user)
        project = Database.models.Project.objects.get(projectName=projectname)
        file = Database.models.File.objects.get(pk=id)

        fileUrl = file.file.path
        linesInFile = self.replaceNewLine(self.readFile(fileUrl))
        print(linesInFile)

        context = {'lines': linesInFile, 'file' : file,'userInformation': userInformation, 'user': user}
        # print(self.readFile(fileUrl))
        return render(request, 'Project/fileDetails.html', context)


    def downloadFiles(self, request, projectname):
        user = request.user
        userInformation = Database.models.UserInformation.objects.get(user=user)
        project = Database.models.Project.objects.get(projectName=projectname)

        pass


#     #################################################

    # def send_file(self, request):
    #
    #     filename = settings.BASE_DIR + < file_name >
    #     download_name = "example.csv"
    #     wrapper = FileWrapper(open(filename))
    #     content_type = mimetypes.guess_type(filename)[0]
    #     response = HttpResponse(wrapper, content_type=content_type)
    #     response['Content-Length'] = os.path.getsize(filename)
    #     response['Content-Disposition'] = "attachment; filename=%s" % download_name
    #     return response

    # def individualDownload(self,request,file):
    #     import zipfile
    #
    #     jungle_zip = zipfile.ZipFile('C:\\Stories\\Fantasy\\jungle.zip', 'w')
    #     jungle_zip.write('C:\\Stories\\Fantasy\\jungle.pdf', compress_type=zipfile.ZIP_DEFLATED)
    #
    #     jungle_zip.close()