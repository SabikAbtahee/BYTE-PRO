from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import Database
from django.contrib.auth.models import User
from django.conf import settings
import difflib
import os
import shutil
from datetime import datetime
from Communication.views import Communication


class Project(object):
    # Rendering Home Page [Project Management]
    def userIsAuthenticated(self, user):
        return user.is_authenticated

    def returnAllUserANdProjects(self):
        allprojects = Database.models.Project.objects.all()
        alluser = Database.models.User.objects.all()
        return alluser, allprojects

    def homePage(self, request):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        projects = Database.models.Project.objects.filter(user=user).order_by('-projectCreatedAt')

        alluser, allprojects = self.returnAllUserANdProjects()


        context = {'userInformation': userInformation,
                   'user': user,
                   'projects': projects,
                   'allprojects':allprojects,
                   'alluser':alluser,
                   'isMaster': True,
                   'isAssigned': False,

                   }
        return render(request, 'Project/home.html', context)

    # Where to create folder while creating project.
    def getProjectUrl(self, username, projectName):
        return '{0}/{1}/{2}/{3}'.format(settings.MEDIA_ROOT, username, 'Projects', projectName)

    # add project
    def addProject(self, request):
        user = request.user

        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')

        userInformation = Database.models.UserInformation.objects.get(user=user)
        if (request.method == 'POST'):
            projectName = request.POST['projectName']
            projectDescription = request.POST['projectDescription']
            accessType = request.POST['accessType']
            project = Database.models.Project(user=user, projectName=projectName,
                                              projectDescription=projectDescription,
                                              accessType=accessType)
            project.save()


            projectUrl = self.getProjectUrl(user.username, projectName)
            if not os.path.exists(projectUrl):
                os.makedirs(projectUrl)
            return redirect('/projectmanagement/')
        else:
            context = {'userInformation': userInformation,
                       'user': user
                       }
            return render(request, 'Project/addProject.html', context)

    # rendering project details
    def projectDetails(self, request, projectname):
        user = request.user

        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')

        userInformation = Database.models.UserInformation.objects.get(user=user)
        # print(projectname)
        project = Database.models.Project.objects.get(user=user, projectName=projectname)
        files = Database.models.File.objects.filter(user=user, project=project).order_by('-modificationTime')
        alluser, allprojects = self.returnAllUserANdProjects()
        assignDevelopers = Database.models.AssignDeveloper.objects.filter(project=project)
        # assignDevelopersUserInformation = Database.models.UserInformation.objects.all()
        isDownloadable = True
        if(files.count()==0): isDownloadable = False

        context = {'userInformation': userInformation,
                   'user': user,
                   'project': project,
                   'files': files,
                   'allprojects':allprojects,
                   'alluser':alluser,
                   'assignDevelopers': assignDevelopers,
                   'isMaster': True,
                   'isAssigned': False,
                   'isDownloadable': isDownloadable
                   }
        return render(request, 'Project/projectDetails.html', context)

    # FIle type and and extension
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
            typeOfFile = 'HTML'
        elif (typeOfFile == 'java' or typeOfFile == 'jsp'):
            typeOfFile = 'JAVA'
        elif (typeOfFile == 'javascript' or typeOfFile == 'js' or typeOfFile == 'jsx'):
            typeOfFile = 'JAVASCRIPT'
        elif (typeOfFile == 'php' or typeOfFile == 'php3' or typeOfFile == 'php4' or typeOfFile == 'php5' or typeOfFile == 'php6'):
            typeOfFile = 'PHP'
        elif (typeOfFile == 'python' or typeOfFile == 'py'):
            typeOfFile = 'PYTHON'
        else:  # rest of the file's types will be considered as C++ file.
            typeOfFile = 'C++'

        return typeOfFile, fileNameWdOutExtention

    # -----------------------------------------------------FILE PURPOSE-------------------------------------------
    # If a file exist in db before
    def fileExistBefore(self, user, project, fileName):
        x = Database.models.File.objects.filter(user=user, project=project, fileName=fileName)
        if (x.count() == 0):
            return False
        else:
            return True

    # return the corresponding files record.
    def getFileRecord(self, user, project, fileName):
        return Database.models.File.objects.get(user=user, project=project, fileName=fileName)

    # remove the file from directory
    def removeFile(self, path):
        print(path)
        os.remove(path)

    # write content in the textfield from file
    def saveFileContent(self, fileBeforeInDatabase):
        lines = self.replaceNewLine(self.readFile(fileBeforeInDatabase.file.path))
        wr = ""
        for line in lines:
            for w in line:
                wr += w
            wr += "\n"
        return wr

    class versionDataClass(object):
        def __init__(self, fileBeforeInDatabase):
            self.version = Database.models.Version()
            self.version.uploader = fileBeforeInDatabase.uploader
            self.version.file = fileBeforeInDatabase
            self.version.versionFileSize = fileBeforeInDatabase.fileSize
            self.version.versionDescription = fileBeforeInDatabase.fileDescription
            self.version.versionFilename = fileBeforeInDatabase.fileName
            self.version.fileContent = Project().saveFileContent(fileBeforeInDatabase)
            self.version.modificationTime = fileBeforeInDatabase.modificationTime

        def save(self):
            self.version.save()

    # RETURN THE BOOLEAN VALUE IF FILE CHANGES.
    def isChanged(self, tempVersion, fileBeforeInDatabase, user, project):

        path = self.getTemporaryFilePath(user.username, project.projectName)

        with open(path, 'w') as tempFile:
            tempFile.write(str(tempVersion.version.fileContent)[:-1])

        file2 = self.replaceTabWithWhiteSpace(self.readFile(fileBeforeInDatabase.file.path))
        file1 = self.replaceTabWithWhiteSpace(self.readFile(path))

        additions, deletations, totalAddition, totalDeletation = self.nDiffDump(file1, file2)
        if (totalDeletation == 0 and totalAddition == 0): return False
        return True

    # single file upload


    def getPrevious_CurrentFileContent(self, tempVersion, fileBeforeInDatabase):
        previous = tempVersion.version.fileContent
        mainProject = Project()
        current = mainProject.replaceNewLine(mainProject.readFile(fileBeforeInDatabase.file.path))

        return previous, current

    class temporaryFileAndVersion(object):
        def __init__(self, uploader, fileBeforeInDatabase, tempVersion, previousFileContent, currentFileContent,
                     isConflict):
            self.uplader = uploader
            self.fileBeforeInDatabase = fileBeforeInDatabase
            self.tempVersion = tempVersion
            self.previousFileContent = previousFileContent
            self.currentFileContent = currentFileContent
            self.isConflict = isConflict

    def doRenderMergePage(self, xx):
        for x in xx:
            if(x.isConflict):
                return True
        return False

    def addFile(self, request, projectname):
        user = request.user
        if(not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')

        userInformation = Database.models.UserInformation.objects.get(user=user)
        project = Database.models.Project.objects.get(user=user, projectName=projectname)
        alluser, allprojects = self.returnAllUserANdProjects()

        tempFileVersions = []
        if (request.method == 'POST'):
            if (len(request.FILES) > 0):
                fileCount = 0
                for file in request.FILES.getlist("file"):

                    fileDescription = request.POST['fileDescription']
                    fileName = file.name
                    fileSize = file.size
                    fileType, fileNameWdOutExtention = self.getFileNameAndType(fileName)

                    isConflict = False

                    if (self.fileExistBefore(user, project, fileName)):

                        fileBeforeInDatabase = self.getFileRecord(user, project, fileName)

                        tempVersion = self.versionDataClass(fileBeforeInDatabase)

                        self.removeFile(fileBeforeInDatabase.file.path)

                        if (fileBeforeInDatabase.uploader != user.username):
                            isConflict = True

                        # overriding
                        fileBeforeInDatabase.file = file
                        fileBeforeInDatabase.fileDescription = fileDescription
                        fileBeforeInDatabase.fileName = fileName
                        fileBeforeInDatabase.fileSize = fileSize  # -----
                        fileBeforeInDatabase.fileType = fileType
                        fileBeforeInDatabase.save()

                        if (self.isChanged(tempVersion, fileBeforeInDatabase, user, project)):
                            fileBeforeInDatabase.modificationTime = datetime.now()
                            previousFileContent, currentFileContent = self.getPrevious_CurrentFileContent(tempVersion,
                                                                                                          fileBeforeInDatabase)

                            tempFileVersions.append(
                                self.temporaryFileAndVersion(user.username,
                                                             fileBeforeInDatabase,
                                                             tempVersion,
                                                             previousFileContent,
                                                             currentFileContent,
                                                             isConflict))
                            fileBeforeInDatabase.uploader = user.username
                            tempVersion.save()

                    else:
                        # new instance
                        File = Database.models.File()
                        File.user = user
                        File.project = project
                        File.uploader = user.username
                        File.file = file
                        File.fileDescription = fileDescription
                        File.fileName = fileName
                        File.fileSize = fileSize
                        File.fileType = fileType
                        File.save()
                        comment=Database.models.Comment.objects.filter(file=File)
                        fileCount+=1



                        self.addProjectTag(user, project.projectName)
                fileCount+=1
                if (self.doRenderMergePage(tempFileVersions)):

                    context = {
                        'user': user,
                        'userInformation': userInformation,
                        'FileWithUsersAndContent': tempFileVersions,
                        'alluser': alluser,
                        'allprojects': allprojects,
                        'isMaster': True,
                        'project': project
                    }

                    return render(request, 'Project/merge.html', context)
                else:
                    Communication().notifiedAllAssignedDevelopers(project, user.username, fileNumbers=fileCount, isMaster=True, type = "upload")
                    return redirect('/projectmanagement/' + project.projectName + '/')
        else:

            context = {'userInformation': userInformation,
                       'user': user,
                       'project': project,
                       'isMaster': True,
                       }
            return render(request, 'Project/addFile.html', context)

    # File read
    def readFile(self, fileUrl):
        f = open(fileUrl, 'r')
        return f.readlines()

    # it replace both new line and tab
    def replaceNewLine(self, linesFile):
        lineWdoutSPNL = []

        for i in range(len(linesFile)):
            tempLine = linesFile[i].replace('\n', '').replace('\t', "    ")
            lineWdoutSPNL.append(tempLine)

        return lineWdoutSPNL

    # rendering file details
    def fileDetails(self, request, projectname, id):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        project = Database.models.Project.objects.get(user=user, projectName=projectname)
        file = Database.models.File.objects.get(pk=id)
        comment=Database.models.Comment.objects.filter(file=file)
        fileUrl = file.file.path
        linesInFile = self.replaceNewLine(self.readFile(fileUrl))
        numberOfLines = len(linesInFile)

        context = {'lines': linesInFile,
                   'file': file,
                   'userInformation': userInformation,
                   'user': user,
                   'project': project,
                   'numberOfLines': numberOfLines,
                   'isMaster': True,
                   'comment':comment

                   }
        # print(self.readFile(fileUrl))
        return render(request, 'Project/fileDetails.html', context)

    # rendering all the versions
    def showVersions(self, request, projectname, id):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        project = Database.models.Project.objects.get(user=user, projectName=projectname)
        file = Database.models.File.objects.get(pk=id)

        versions = Database.models.Version.objects.filter(file=file).order_by('-id')

        noVersions = False

        if (versions.count() == 0):
            noVersions = True

        context = {
            'user': user,
            'userInformation': userInformation,
            'project': project,
            'versions': versions,
            'file': file,
            'noVersions': noVersions,
            'isMaster': True
        }
        return render(request, 'Project/showVersions.html', context)

    def nDiffDump(self, file1, file2):
        diff = difflib.ndiff(file1, file2)
        p0 = 0

        class add(object):
            def __init__(self, line, isAddition):
                self.line = line
                self.isAddition = isAddition

        class delete(object):
            def __init__(self, line, isDeletation):
                self.line = line
                self.isDeletation = isDeletation

        additions = []
        deletations = []

        totalAddition = 0
        totalDeletation = 0

        for line in diff:
            p0 += 1
            if (line[0] == '-'):
                deletations.append(delete(line, True))
                totalDeletation += 1
            elif (line[0] == ' '):
                deletations.append(delete(line, False))
                additions.append(add(line, False))
            elif (line[0] == '+'):
                additions.append(add(line, True))
                totalAddition += 1

        return additions, deletations, totalAddition, totalDeletation

    def getTemporaryFilePath(self, username, projectname):
        return os.path.join(settings.BASE_DIR, 'media', username, projectname, 'temp.bp')

    def replaceTabWithWhiteSpace(self, lines):
        arr = []
        for line in lines:
            line = line.replace('\t', '    ')
            arr.append(line)
        return arr

    def compareWithPreviousVersion(self, request, projectname, id):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        project = Database.models.Project.objects.get(user=user, projectName=projectname)
        file = Database.models.File.objects.get(pk=id)

        path = self.getTemporaryFilePath(user.username, project.projectName)

        versions = Database.models.Version.objects.filter(file=file).order_by('-id')

        noVersions = False

        if (versions.count() != 0):
            noVersions = True
            with open(path, 'w') as tempFile:
                tempFile.write(str(versions[0].fileContent))

            file2 = self.replaceTabWithWhiteSpace(self.readFile(file.file.path))
            file1 = self.replaceTabWithWhiteSpace(self.readFile(path))

            additions, deletations, totalAddition, totalDeletation = self.nDiffDump(file1, file2)
            self.removeFile(path)
        else:
            file2 = self.replaceTabWithWhiteSpace(self.readFile(file.file.path))
            additions, deletations, totalAddition, totalDeletation = self.nDiffDump([], file2)

        context = {
            'additions': additions,
            'deletations': deletations,
            'totalAddition': totalAddition,
            'totalDeletation': totalDeletation,
            'user': user,
            'userInformation': userInformation,
            'project': project,
            'file': file
        }
        return render(request, 'Project/compareFile.html', context)

    def createZipFile(self, username, projectName):
        zippath = os.path.join(settings.BASE_DIR, 'media', username, projectName, 'download')
        directoryOfFiles = os.path.join(settings.BASE_DIR, 'media', username, projectName)
        shutil.make_archive(zippath, 'zip', directoryOfFiles)

    def openZipFile(self, username, projectName):
        return open(os.path.join(settings.BASE_DIR, 'media', username, projectName, 'download.zip'), 'rb')

    def downloadFiles(self, request, projectname):

        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        project = Database.models.Project.objects.get(user=user, projectName=projectname)
        # shutil.make_archive(os.path.join(settings.BASE_DIR, 'media', user.username, project.projectName, 'download'),'zip',  os.path.join(settings.BASE_DIR, 'media', user.username, project.projectName))
        self.createZipFile(user.username, project.projectName)

        zip_file = self.openZipFile(user.username, project.projectName)

        # zip_file  = open(os.path.join(settings.BASE_DIR, 'media', user.username, project.projectName, 'download1.zip').format(str(timestamp).encode('utf-8').strip()))
        response = HttpResponse(zip_file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="%s"' % 'download.zip'
        return response

    def editFile(self, request, projectname, id):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        project = Database.models.Project.objects.get(user=user, projectName=projectname)
        file = Database.models.File.objects.get(pk=id)

        if (request.method == 'POST'):
            editedCode = request.POST['code']
            fileDescription = request.POST['fileDescription']

            tempVersion = self.versionDataClass(file)

            with open(file.file.path, 'w') as tempFile:
                tempFile.write(editedCode.replace('\n', ''))

            if (self.isChanged(tempVersion, file, user, project)):
                file.fileDescription = fileDescription
                file.fileSize = len(editedCode)
                file.modificationTime = datetime.now()
                tempVersion.save()
                file.save()
                return redirect('/projectmanagement/' + project.projectName + '/')

        fileUrl = file.file.path
        linesInFile = self.replaceNewLine(self.readFile(fileUrl))
        numberOfLines = len(linesInFile)

        context = {'lines': linesInFile, 'file': file, 'userInformation': userInformation, 'user': user,
                   'project': project, 'numberOfLines': numberOfLines}
        # print(self.readFile(fileUrl))
        return render(request, 'Project/editFile.html', context)

    def rebaseFile(self, request, projectname, fid, vid):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        project = Database.models.Project.objects.get(user=user, projectName=projectname)
        file = Database.models.File.objects.get(pk=fid)
        version = Database.models.Version.objects.get(pk=vid)

        tempVersion = self.versionDataClass(file)
        tempVersion.save()
        with open(file.file.path, 'w') as tempFile:
            tempFile.write(str(version.fileContent)[:-1])

        return redirect('/projectmanagement/' + project.projectName + '/' + fid + '/')

    def deleteFile(self, request, projectname, id):

        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        project = Database.models.Project.objects.get(user=user, projectName=projectname)
        file = Database.models.File.objects.get(pk=id, user=user, project=project)
        self.removeFile(file.file.path)
        file.delete()
        return redirect('/projectmanagement/' + project.projectName + '/')


    def fetchLanguage(self, request):
        pid = request.GET.get('pid', None)
        project = Database.models.Project.objects.get(pk=pid)
        files = Database.models.File.objects.filter(project = project)
        data = {}
        for file in files:
            type = file.fileType
            if(type not in data):
                data[type] = 0
                data[type]+=1

        data['success'] = True
        print(data)
        return JsonResponse(data, safe=False)


    def projectSettings(self, request, projectname):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        project = Database.models.Project.objects.get(user=user, projectName=projectname)
        files = Database.models.File.objects.filter(project = project)
        alluser, allprojects = self.returnAllUserANdProjects()
        assignDevelopers = Database.models.AssignDeveloper.objects.filter(project=project)
        print(assignDevelopers)


        context = {'userInformation': userInformation,
                   'user': user,
                   'project': project,
                   'allprojects': allprojects,
                   'alluser': alluser,
                   'assignDevelopers': assignDevelopers,
                   'files': files

                   }

        return render(request, 'Project/projectSettings.html', context)

    def deleteDeveloper(self, request, projectname, aid):

        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')


        assignDevelopers = Database.models.AssignDeveloper.objects.get(pk=aid)

        assignDevelopers.delete()
        return redirect('/projectmanagement/' + projectname + '/projectsettings/')
    # Project progress functionality
    def projectProgress(self,request,projectname):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        project = Database.models.Project.objects.get(user=user, projectName=projectname)
        file=Database.models.File.objects.filter(user=user,project=project)


        if request.method=='POST':

            if request.POST.get("TO-DO-BUTTON"):
                description = request.POST.get('todoDescription')
                if(len(description)>0):
                    todo = Database.models.Todo(user=user, project=project,todo_description = description)
                    todo.save()
            if request.POST.get("IN-PROGRESS-BUTTON"):
                description = request.POST.get('inProgressDescription')
                fileNames = request.POST.getlist('filenames1')
                files = ""
                for i in fileNames:
                    files +=i+","
                if (len(description) > 0):
                    inprogress = Database.models.InProgress(user=user, project=project,inProgress_description=description,fileNames=files)
                    inprogress.save()

            if request.POST.get("DONE-BUTTON"):
                description = request.POST.get('doneDescription')
                fileNames = request.POST.getlist('filenames2')
                files=""
                for i in fileNames:
                    files+=i+","
                if (len(description) > 0):
                    done = Database.models.Done(user=user, project=project,done_description=description,fileNames=files)
                    done.save()

            if request.POST.get("DELETE-BUTTON-TODO"):
                description=request.POST.get('todoDescriptionDelete')
                Database.models.Todo.objects.filter(todo_description = description).delete()

            if request.POST.get("DELETE-BUTTON-IN"):
                description=request.POST.get('inProgressDescriptionDelete')
                fileNames=request.POST.get('inProgressFilesDelete')
                Database.models.InProgress.objects.filter(inProgress_description = description,fileNames=fileNames).delete()

            if request.POST.get("DELETE-BUTTON-DONE"):
                description=request.POST.get('doneDescriptionDelete')
                fileNames = request.POST.get('doneFilesDelete')
                Database.models.Done.objects.filter(done_description = description,fileNames=fileNames).delete()

            if request.POST.get("CHECK-BUTTON-TODO"):
                description=request.POST.get('todoDescriptionDelete')
                if (len(description) > 0):
                    done = Database.models.Done(user=user, project=project,done_description=description)
                    done.save()
                Database.models.Todo.objects.filter(todo_description=description).delete()

            if request.POST.get("CHECK-BUTTON-IN"):
                description=request.POST.get('inProgressDescriptionDelete')
                fileNames=request.POST.get('inProgressFilesDelete')

                if (len(description) > 0):
                    done = Database.models.Done(user=user, project=project, done_description=description,
                                                fileNames=fileNames)
                    done.save()
                Database.models.InProgress.objects.filter(inProgress_description=description,
                                                          fileNames=fileNames).delete()
                # if request.POST.get("CHECK-BUTTON-DONE"):
                #     description=request.POST.get('doneDescriptionDelete')
                #     fileNames = request.POST.get('doneFilesDelete')
                #     Database.models.Done.objects.filter(done_description = description,fileNames=fileNames).delete()


        todo = Database.models.Todo.objects.filter(user=user, project=project)
        inprogress = Database.models.InProgress.objects.filter(user=user, project=project)
        done = Database.models.Done.objects.filter(user=user, project=project)


        context = {'userInformation': userInformation,
                   'user': user,
                   'project': project,
                   'file': file,
                   'todo':todo,
                   'inprogress': inprogress,
                   'done': done,
                   }


        return render(request,'Project/projectProgress.html',context)
    # Adds project tag everytime a file is added
    def addProjectTag(self,user,projectname):

        project = Database.models.Project.objects.get(user=user, projectName=projectname)
        files = Database.models.File.objects.filter(user=user, project=project)
        allTypes=[]
        for type in files:
            if type.fileType not in allTypes:
                allTypes.append(type.fileType)
        # print(allTypes)
        project.skilltag=allTypes
        project.save()
        # print(project.skilltag)

    def commentOnFile(self,request,projectname,id):
        user=request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        project = Database.models.Project.objects.get(user=user,projectName=projectname)
        file = Database.models.File.objects.get(user=user, project=project,pk=id)

        if (request.method=='POST'):
            if request.POST.get("COMMENT-BUTTON"):
                description = request.POST.get('COMMENT-DESCRIPTION')
                comment=Database.models.Comment(file=file,commentDescription=description,commentTime=datetime.now(),commentator=user.username)
                comment.save()
                Communication().notifiedAllAssignedDevelopers(project, user.username, fileNumbers=0, isMaster=True,
                                                              type="comment")

        return redirect('/projectmanagement/' + project.projectName + '/'+id+'/')

    def projectIssue(self, request, projectname):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return HttpResponse('You need to login')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        project = Database.models.Project.objects.get(user=user, projectName=projectname)
        ISSUE = Database.models.Issue.objects.filter(project=project).order_by('-id')
        alluser, allprojects = self.returnAllUserANdProjects()

        if (request.method == 'POST'):
            issueDescription = request.POST['issueDescription']
            label = request.POST['label']

            issue = Database.models.Issue()
            issue.issueDescription = issueDescription
            issue.issueCreator = user
            issue.project = project
            issue.label = label
            issue.isClosed = False
            issue.save()
            Communication().notifiedAllAssignedDevelopers(project, user.username, fileNumbers=0, isMaster=True,
                                                          type="issue")

        context = {'userInformation': userInformation,
                   'user': user,
                   'project': project,
                   'allprojects': allprojects,
                   'alluser': alluser,
                   'Issues': ISSUE,
                   'isFile': False,
                   'isMaster': True
                   }

        return render(request, 'Project/Issue.html', context)

    def closeIssue(self, request):
        issueId = request.POST.get('issueId', None)

        Issue = Database.models.Issue.objects.get(pk=issueId)
        Issue.isClosed = True
        Issue.save()

        data = {
            'success': True
        }
        return JsonResponse(data)

    def fileIssues(self, request, projectname, id):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return HttpResponse('You need to login')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        project = Database.models.Project.objects.get(user=user, projectName=projectname)
        file = Database.models.File.objects.get(pk=id)
        ISSUE = Database.models.Issue.objects.filter(project=project, fileName=file.fileName).order_by('-id')
        alluser, allprojects = self.returnAllUserANdProjects()
        if (request.method == 'POST'):
            issueDescription = request.POST['issueDescription']
            label = request.POST['label']

            issue = Database.models.Issue()
            issue.issueDescription = issueDescription
            issue.issueCreator = user
            issue.project = project
            issue.label = label
            issue.isClosed = False
            issue.fileName = file.fileName
            issue.save()
            Communication().notifiedAllAssignedDevelopers(project, user.username, fileNumbers=0, isMaster=True,
                                                          type="issue")
        context = {'userInformation': userInformation,
                   'user': user,
                   'project': project,
                   'allprojects': allprojects,
                   'alluser': alluser,
                   'Issues': ISSUE,
                   'isFile': True,
                   'file': file,
                   'isMaster': True,
                   'isAssigned': False,
                   'isAnonymous': False,
                   }

        return render(request, 'Project/Issue.html', context)


    def projectCheck(self, request):
        user = request.user

        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')

        projectName = request.POST.get('projectName', None)
        allprojects = Database.models.Project.objects.all()
        match=False
        for i in allprojects:

            if(str(i)==str(projectName)):
                match=True

        # print(allprojects.projectsName)
        # if (y is None):
        #     error = "Old password does not match"
        #     bools = False
        # else:
        #     error = "Old password Matches"
        #     bools = True

        data = {

            'check': match,
        }

        return JsonResponse(data)