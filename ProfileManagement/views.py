from django.shortcuts import render
from passlib.hash import pbkdf2_sha256
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.
import Database
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse


class ProfileManagement(object):
    def userIsAuthenticated(self, user):
        return user.is_authenticated

    def get_pro_pic(self, pic):
        return 'pro_pic.' + pic.name.split('.')[1]

    def profileView(self, request):
        user = request.user

        if (not self.userIsAuthenticated(user)):
            return HttpResponse('You need to login')

        userInformation = Database.models.UserInformation.objects.get(user=user)
        context = {'userInformation': userInformation, 'user': user}
        if (request.method == 'POST'):
            # ##################################PASSWORD CHANGE FORM#######################
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                user = form.save()
                user.is_active = False
            if (len(request.FILES) != 0):
                pic = request.FILES['pictureUpload']
                # print(pic)
                userInformation.profilePicture = pic

            name = request.POST['name']
            biography = request.POST['biography']
            skilltags = request.POST.getlist('skillTags')

            userInformation.name = name
            userInformation.biography = biography
            if (len(skilltags) > 0):
                userInformation.skilltag = skilltags

            userInformation.save()
            # return render(request, 'ProfileManagement/profileView.html', context)
        else:
            form = PasswordChangeForm(user=request.user)
            context['form'] = form
        update_session_auth_hash(request, user)
        return render(request, 'ProfileManagement/profileView.html', context)

    def passwordCheck(self, request):
        user = request.user

        if (not self.userIsAuthenticated(user)):
            return HttpResponse('You need to login')

        password = request.POST.get('oldPass', None)

        y = authenticate(request, username=user, password=password)

        if (y is None):
            error = "Old password does not match"
            bools = False
        else:
            error = "Old password Matches"
            bools = True
        data = {
            'is_taken': error,
            'check': bools,
        }

        return JsonResponse(data)