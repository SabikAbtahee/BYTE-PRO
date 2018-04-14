from django.shortcuts import render

# Create your views here.
import Database
from django.contrib.auth.models import User

class ProfileManagement(object):

    def get_pro_pic(self,pic):
        return 'pro_pic.'+pic.name.split('.')[1]

    def profileView(self,request):
        user = request.user
        userInformation = Database.models.UserInformation.objects.get(user=user)

        context = {'userInformation': userInformation, 'user': user }
        if(request.method=='POST'):
            if(len(request.FILES)!=0):
                pic = request.FILES['pictureUpload']
                # print(pic)
                userInformation.profilePicture = pic
            name=request.POST['name']
            biography=request.POST['biography']







            userInformation.name = name
            userInformation.biography = biography
            # print(userInformation.profilePicture)
            skilltags=request.POST.getlist('skillTags')
            #print(skilltags)
            # userInformation.skilltag='asdf'
            #print(userInformation.skilltag)
            userInformation.skilltag=skilltags
           # print(userInformation.skilltag)




            # x=userInformation.skilltag(skilltags='JAVA')
            # x.save()
            # print(skilltags[0])
            userInformation.save()




        return render(request, 'ProfileManagement/profileView.html',context)