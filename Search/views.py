# from _nsis import allusers

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import Database
from _datetime import datetime
from Communication.views import Communication


from Project.views import Project
class Search(object):
    # check if user is authenticated
    def userIsAuthenticated(self, user):
        return user.is_authenticated

    #retrieve all users and projects
    def returnAllUserANdProjects(self):
        allprojects = Database.models.Project.objects.all()
        alluser = Database.models.User.objects.all()
        return alluser, allprojects

    #is the developer assigned
    def isAssingedDeveloper(self, user, project):
        totalAssignedDev =  Database.models.AssignDeveloper.objects.filter(project=project)
        specificUserAssigned= Database.models.AssignDeveloper.objects.filter(project=project, assignDeveloper=user)

        return totalAssignedDev, specificUserAssigned.count() > 0

    #searching operation -> user, project etc
    def search(self,request):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        alluser, allprojects = self.returnAllUserANdProjects()
        searchInput=request.POST['searchinput']
        numberOfUsers=Database.models.User.objects.filter(username=searchInput)
        numberofProjects = Database.models.Project.objects.filter(projectName=searchInput)
        if(numberOfUsers.count()>0):
            return self.renderToUser(request, searchInput)

        elif(numberofProjects.count()>0):
            allProjects = numberofProjects
            context = {'userInformation': userInformation,
                       'user': user,
                       'alluser':alluser,
                       'allprojects': allProjects}

            return render(request, 'Search/searchedAllProjectsShow.html', context)
        else:
            context = {'userInformation': userInformation,
                       'user': user,
                       'alluser': alluser,
                       }
            return render(request, 'Search/searchedNotFound.html',context)

    def renderToUser(self, request, username):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request, 'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        alluser, allprojects = self.returnAllUserANdProjects()

        numberOfUsers = Database.models.User.objects.filter(username=username)

        if (numberOfUsers.count() > 0):
            searchedUser = numberOfUsers[0]
            searchedUserProjects = Database.models.Project.objects.filter(user=searchedUser,
                                                                          accessType="Public").order_by(
                '-projectCreatedAt')
            searchedUserInformation = Database.models.UserInformation.objects.get(user=searchedUser)
            isMaster = False

            if (user == searchedUser):
                isMaster = True

            if (isMaster == False):

                context = {'userInformation': userInformation,
                           'user': user,
                           'projects': searchedUserProjects,
                           'allprojects': allprojects,
                           'alluser': alluser,
                           'searchedUser': searchedUser,
                           'searchedUserInformation': searchedUserInformation,
                           'isMaster': isMaster}

                return render(request, 'Project/home.html', context)
            else:
                return redirect('/projectmanagement/')

    #how other user except master saw project details
    def searchedProjectDetails(self, request, username, projectname):

        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)

        alluser, allprojects = self.returnAllUserANdProjects()

        searchedUser = Database.models.User.objects.get(username=username)

        searchedUserInformation = Database.models.UserInformation.objects.get(user=searchedUser)
        searchedProject = Database.models.Project.objects.get(user=searchedUser, projectName=projectname)
        __isAssignInPrivateProject = Database.models.AssignDeveloper.objects.filter(project = searchedProject, assignDeveloper = user).count() > 0
        if (searchedProject.accessType=="Private" and  __isAssignInPrivateProject==False ):
            context = {'userInformation': userInformation,
                       'user': user,
                       'alluser': alluser,
                       'allprojects': allprojects
                       }
            return render(request, 'Search/accessDenied.html', context)
        files = Database.models.File.objects.filter(user=searchedUser, project=searchedProject).order_by('-id')
        isMaster = False
        isDownloadable = True
        if (files.count() == 0): isDownloadable = False
        if (user == searchedUser):
            isMaster = True

        if (isMaster == False):
            totalAssigned, isAssigned = self.isAssingedDeveloper(user, searchedProject)

            context = {'userInformation': userInformation,
                       'user': user,
                       'searchedUser': searchedUser,
                       'searchedUserInformation': searchedUserInformation,
                       'project': searchedProject,
                       'files': files,
                       'isMaster': isMaster,
                       'isAssigned': isAssigned,
                       'assignDevelopers': totalAssigned,
                       'alluser': alluser,
                       'allprojects': allprojects,
                       'isDownloadable': isDownloadable
                       }

            return render(request, 'Project/projectDetails.html', context)
        else:
            return redirect('/projectmanagement/'+searchedProject.projectName+'/')

    # how other user except master saw project details
    def searchedFileDetails(self, request, username, projectname , id):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)

        file = Database.models.File.objects.get(pk=id)
        searchedProject = file.project
        searchedUser = file.user
        fileUrl = file.file.path
        mainProject =  Project()
        linesInFile = mainProject.replaceNewLine(mainProject.readFile(fileUrl))
        numberOfLines = len(linesInFile)
        comment=Database.models.Comment.objects.filter(file=file)
        _ , isAssigned = self.isAssingedDeveloper(user, file.project)
        isMaster = False
        if (user == searchedUser):
            isMaster = True

        context = {'lines': linesInFile,
                   'file': file,
                   'userInformation': userInformation,
                   'user': user,
                   'searchedUser': searchedUser,
                   'project': searchedProject,
                   'numberOfLines': numberOfLines,
                   'isMaster': isMaster,
                   'isAssigned': isAssigned,
                   'comment':comment}

        return render(request, 'Project/fileDetails.html', context)

    # file add procedure --> different user file merging, storing version etc
    def addFile(self, request, username, projectname):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)

        alluser, allprojects = self.returnAllUserANdProjects()

        searchedUser = Database.models.User.objects.get(username=username)
        searchedProject = Database.models.Project.objects.get(user=searchedUser, projectName=projectname)
        _, isAssigned = self.isAssingedDeveloper(user, searchedProject)
        mainProject = Project()
        tempFileVersions = []
        if (request.method == 'POST'):
            if (len(request.FILES) > 0):
                fileCount = 0
                for file in request.FILES.getlist("file"):

                    fileDescription = request.POST['fileDescription']
                    fileName = file.name
                    fileSize = file.size
                    fileType, fileNameWdOutExtention = mainProject.getFileNameAndType(fileName)
                    isConflict = False
                    if (mainProject.fileExistBefore(searchedUser, searchedProject, fileName)):

                        fileBeforeInDatabase = mainProject.getFileRecord(searchedUser, searchedProject, fileName)

                        tempVersion = mainProject.versionDataClass(fileBeforeInDatabase)

                        mainProject.removeFile(fileBeforeInDatabase.file.path)

                        if (fileBeforeInDatabase.uploader != user.username):
                            isConflict = True

                        # overriding
                        fileBeforeInDatabase.file = file
                        fileBeforeInDatabase.fileDescription = fileDescription
                        fileBeforeInDatabase.fileName = fileName
                        fileBeforeInDatabase.fileSize = fileSize #-----
                        fileBeforeInDatabase.fileType = fileType
                        fileBeforeInDatabase.save()

                        if (mainProject.isChanged(tempVersion, fileBeforeInDatabase, searchedUser, searchedProject)):
                            fileBeforeInDatabase.modificationTime = datetime.now()
                            previousFileContent, currentFileContent = mainProject.getPrevious_CurrentFileContent(tempVersion, fileBeforeInDatabase)

                            tempFileVersions.append(
                                mainProject.temporaryFileAndVersion(user.username,
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
                        File.user = searchedUser
                        File.project = searchedProject
                        File.uploader = user.username
                        File.file = file
                        File.fileDescription = fileDescription
                        File.fileName = fileName
                        File.fileSize = fileSize
                        File.fileType = fileType
                        File.save()
                    fileCount+=1
                if(mainProject.doRenderMergePage(tempFileVersions)):
                    context = {
                        'user': user,
                        'userInformation': userInformation,
                        'FileWithUsersAndContent': tempFileVersions,
                        'alluser': alluser,
                        'allprojects': allprojects,
                        'searchedUser': searchedUser,
                        'project': searchedProject,
                        'isMaster': False
                    }
                    return render(request, 'Project/merge.html', context)
                else:
                    Communication().notifiedAllAssignedDevelopers(searchedProject, user.username, fileNumbers=fileCount, isMaster=False,
                                                                  type="upload")
                    return redirect('/search/' + searchedUser.username + '/' + searchedProject.projectName)

        else:
            if (user == searchedUser):  # when user is master
                return redirect('/projectmanagement/' + searchedProject.projectName + '/addfiles/')
            elif (isAssigned):  # when user is assigned
                context = {'userInformation': userInformation,
                           'user': searchedUser,
                           'project': searchedProject,
                           'alluser': alluser,
                           'allprojects': allprojects,
                           'isMaster': False}
                return render(request, 'Project/addFile.html', context)
            else:  # else
                context = {'userInformation': userInformation,
                           'user': user,
                           'alluser': alluser,
                           'allprojects':allprojects
                           }
                return render(request, 'Search/accessDenied.html', context)

    #merging, its an ajax call merging function
    def merge(self, request):
        code = request.POST.get('code', None)
        fileId = request.POST.get('fileId', None)

        file = Database.models.File.objects.get(pk = fileId)
        file.uploader = request.user.username
        with open(file.file.path, 'w') as tempFile:
            tempFile.write(code)
        file.save()
        data ={
            'success': '<strong>'+file.fileName+'</strong> Updated successfully'
        }
        return JsonResponse(data)

    #show versions nu other users
    def showVersions(self, request, username, projectname, id):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)

        alluser, allprojects = self.returnAllUserANdProjects()

        file = Database.models.File.objects.get(pk=id)
        versions = Database.models.Version.objects.filter(file=file).order_by('-id')
        noVersions = False

        searchedUser = file.user
        _, isAssigned = self.isAssingedDeveloper(user, file.project)
        isMaster = False
        if (user == searchedUser):
            isMaster = True

        if (isAssigned == False and isMaster == False):
            return HttpResponse('Access Denied')

        if (versions.count() == 0):
            noVersions = True

        context = {
            'user': user,
            'userInformation': userInformation,
            'versions': versions,
            'file': file,
            'alluser': alluser,
            'allprojects': allprojects,
            'isMaster': isMaster,
            'noVersions': noVersions
        }

        return render(request, 'Project/showVersions.html', context)

    #previous versions comparisons by other users
    def compareWithPreviousVersion(self, request, username, projectname, id):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userInformation = Database.models.UserInformation.objects.get(user=user)
        alluser, allprojects = self.returnAllUserANdProjects()


        file = Database.models.File.objects.get(pk=id)
        searchedUser = file.user
        searcheProject = file.project

        _, isAssigned = self.isAssingedDeveloper(user, file.project)
        isMaster = False
        if (user == searchedUser):
            isMaster = True

        if (isAssigned == False and isMaster == False):
            return HttpResponse('Access Denied')

        mainProject = Project()
        path = mainProject.getTemporaryFilePath(searchedUser.username, searcheProject.projectName)
        versions = Database.models.Version.objects.filter(file=file).order_by('-id')

        if (versions.count() != 0):

            with open(path, 'w') as tempFile:
                tempFile.write(str(versions[0].fileContent))

            file2 = mainProject.replaceTabWithWhiteSpace(mainProject.readFile(file.file.path))
            file1 = mainProject.replaceTabWithWhiteSpace(mainProject.readFile(path))

            additions, deletations, totalAddition, totalDeletation = mainProject.nDiffDump(file1, file2)
            mainProject.removeFile(path)
        else:
            file2 = mainProject.replaceTabWithWhiteSpace(mainProject.readFile(file.file.path))
            additions, deletations, totalAddition, totalDeletation = mainProject.nDiffDump([], file2)

        context = {
            'additions': additions,
            'deletations': deletations,
            'totalAddition': totalAddition,
            'totalDeletation': totalDeletation,
            'user': user,
            'userInformation': userInformation,
            'alluser': alluser,
            'allprojects': allprojects,
            'project': searcheProject,
            'file': file
        }
        return render(request, 'Project/compareFile.html', context)

    def projectIssue(self, request, username, projectname):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return HttpResponse('You need to login')
        userInformation = Database.models.UserInformation.objects.get(user=user)

        searchedUser = Database.models.User.objects.get(username=username)

        project = Database.models.Project.objects.get(user=searchedUser, projectName=projectname)
        ISSUE = Database.models.Issue.objects.filter(project=project).order_by('-id')
        alluser, allprojects = self.returnAllUserANdProjects()

        _, isAssigned = self.isAssingedDeveloper(user, project)
        isMaster = False
        isAnonymous = True
        if (user == searchedUser):
            isMaster = True

        if (isAssigned == False and isMaster == False):
            isAnonymous = True

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
            Communication().notifiedAllAssignedDevelopers(project, user.username, fileNumbers=0, isMaster=False,
                                                          type="issue")

        context = {'userInformation': userInformation,
                   'user': user,
                   'project': project,
                   'allprojects': allprojects,
                   'alluser': alluser,
                   'Issues': ISSUE,
                   'isFile': False,
                   'isMaster': isMaster,
                   'isAssigned': isAssigned,
                   'isAnonymous': isAnonymous,
                   'searchedUser': searchedUser
                   }

        return render(request, 'Project/Issue.html', context)

    def fileIssue(self, request, username, projectname, id):
        user = request.user
        if (not self.userIsAuthenticated(user)):
            return HttpResponse('You need to login')
        userInformation = Database.models.UserInformation.objects.get(user=user)

        file = Database.models.File.objects.get(pk=id)
        searchedUser = file.user
        project = Database.models.Project.objects.get(user=searchedUser, projectName=projectname)

        ISSUE = Database.models.Issue.objects.filter(project=project, fileName=file.fileName).order_by('-id')
        alluser, allprojects = self.returnAllUserANdProjects()

        _, isAssigned = self.isAssingedDeveloper(user, file.project)
        isMaster = False
        isAnonymous = True
        if (user == searchedUser):
            isMaster = True

        if (isAssigned == False and isMaster == False):
            isAnonymous = True

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
            print(issue.issueDescription, issue.fileName)
            Communication().notifiedAllAssignedDevelopers(project, user.username, fileNumbers=0, isMaster=False,
                                                          type="issue")
        context = {'userInformation': userInformation,
                   'user': user,
                   'project': project,
                   'allprojects': allprojects,
                   'alluser': alluser,
                   'Issues': ISSUE,
                   'isFile': True,
                   'file': file,
                   'isMaster': isMaster,
                   'isAssigned': isAssigned,
                   'isAnonymous': isAnonymous,
                   'searchedUser': searchedUser
                   }


        return render(request, 'Project/Issue.html', context)
    #download zip file
    def downloadFiles(self, request, username, projectname):

        user = request.user

        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')

        searchedUser = Database.models.User.objects.get(username=username)
        searchedProject = Database.models.Project.objects.get(user=searchedUser, projectName=projectname)
        mainProject = Project()
        mainProject.createZipFile(searchedUser.username, searchedProject.projectName)

        zip_file = mainProject.openZipFile(searchedUser.username, searchedProject.projectName)

        response = HttpResponse(zip_file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="%s"' % 'download.zip'
        return response

    def commentOnFile(self,request,username,projectname,id):


        user=request.user
        if (not self.userIsAuthenticated(user)):
            return render(request,'Authentication/loggedOut.html')
        userProject=Database.models.User.objects.get(username=username)
        project = Database.models.Project.objects.get(user=userProject,projectName=projectname)
        file = Database.models.File.objects.get(user=userProject, project=project,pk=id)

        if (request.method=='POST'):
            if request.POST.get("COMMENT-BUTTON"):

                description = request.POST.get('COMMENT-DESCRIPTION')
                comment = Database.models.Comment(file=file, commentDescription=description, commentTime=datetime.now(),
                                                  commentator=user.username)
                comment.save()
                Communication().notifiedAllAssignedDevelopers(project, user.username, file.id, isMaster=False,
                                                              type="comment")
        return redirect('/search/' + userProject.username+'/'+project.projectName + '/' + id + '/')