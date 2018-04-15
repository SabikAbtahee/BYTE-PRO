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
            skilltags = request.POST.getlist('skillTags')

            userInformation.name = name
            userInformation.biography = biography
            if(len(skilltags)>0):
                userInformation.skilltag=skilltags

            userInformation.save()




        return render(request, 'ProfileManagement/profileView.html',context)