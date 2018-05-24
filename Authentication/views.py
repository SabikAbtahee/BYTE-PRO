from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User
#from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.tokens import default_token_generator
from django.db.models.query_utils import Q
#from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import loader
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.views.generic import *
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from .forms import PasswordResetRequestForm, SetPasswordForm, SignupForm
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import logout
# ------------------ Email ------------------
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# ----------------DATABASE IMPORTED---------------------------

import Database



class Authentication(object):

    # ----------------------------------------------------------------------------------Sign Up------------------------------------------------------------------------------

    def signUp(self, request):
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                userInformation=Database.models.UserInformation(user=user)
                userInformation.save()
                current_site = get_current_site(request)
                print('çurrent site:', current_site)
                # Here can be a new function that can be called to resend later
                message = render_to_string('Authentication/AccountActivation/acc_active_email.html', {
                    'user':user, 'domain':current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })

                to_email = form.cleaned_data.get('email')
                subject = "Activate your BYTE PRO account."
                # self.sendEmail(message, to_email , subject)
                print(message)

                return render(request, 'Authentication/ActivationLink.html', {'email': user.email, 'pk': user.pk})
        else:
            form = SignupForm()
        return render(request, 'Authentication/signUp.html', {'form': form})
    # ----------------------------------------------------------------------------------Send Email------------------------------------------------------------------------------
    def sendEmail(self, body, reciever, subject):
        fromaddr = "bytepro123@gmail.com"

        toaddr = str(reciever)
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject

        body = body
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "cs819829")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()


    # --------------------------------------------------------------------- Account Activation After Signing Up------------------------------------------------------------------------------
    def activate(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
            return render(request, 'Authentication/ActivationConfirmedLink.html')
        else:
            return HttpResponse('Activation link is invalid!')

    # --------------------------------------------------------------------------------------Try-Temporary--------------------------------------------------------------------------------------------
    def adduser(self,request):
        if(request.method=="POST"):
            # request.POST.get('is_private', False)
            name = request.POST.get("name", False)
            username = request.POST.get('username', False)
            password = request.POST.get("password", False)
            email = request.POST.get("email", False)
            confirmPassword = request.POST.get("confirmPassword", False)

            enc_password = pbkdf2_sha256.encrypt(password, rounds = 1200, salt_size = 32)
            print(enc_password)
            print(pbkdf2_sha256.decrypt(enc_password))

            user1 = Database.models.UsersAll(name=name, userName=username, password=enc_password, email=email)
            user1.save()

    def index(self,request):
        print(request.user.email)
        user1 = request.user
        print(user1)


        userInformation = Database.models.UserInformation.objects.get(user=user1)
        print(userInformation.name)
        context={'userInformation':userInformation}

        return render(request, 'Authentication/index.html',context)

    def resendRecovery(self, request):
        if(request.method=="POST"):
            email = request.POST.get('email', False)
            ResetPasswordRequestView().reset_password(request, request.user)

    def resendActivation(self, request):
        print("called")
        if (request.method == "POST"):
            email = request.POST.get('email_or_username', False)
            # pk = request.POST.get('pk', False)


            current_site = get_current_site(request)
            # Here can be a new function that can be called to resend later
            user = Database.models.User.objects.get(email=email)
            message = render_to_string('Authentication/AccountActivation/acc_active_email.html', {
                'user': user, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })

            to_email = email
            subject = "Activate your BYTE PRO account."
            # self.sendEmail(message, to_email , subject)
            print(to_email)
            print(message)
            return render(request, 'Authentication/ActivationLink.html', {'email': email})

    def checkEmail(self, request):
        print("called")
        email = request.GET.get('email', None)
        isExist = Database.models.User.objects.filter(email = email).count() > 0
        print(email)
        print(isExist)
        data = {
            'isExist': isExist
        }
        return JsonResponse(data)

    def logout(self,request):

        response = logout(request)

        return render(response, 'Authentication/signOut.html')
# --------------------------------------------------------------- **************** ----------------------------------------------------------




# ----------------------------------------------------------------------------------- Password Recovery ----------------------------------------------------------------------
class ResetPasswordRequestView(FormView):

    template_name = "registration/password_reset_form.html"
    success_url = '/admin/'
    form_class = PasswordResetRequestForm

    @staticmethod
    def validate_email_address(email):

        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def send_email(self, body, reciever):
        fromaddr = "bytepro123@gmail.com"

        toaddr = reciever
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Reset Your Password"

        body = body
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "cs819829")
        text = msg.as_string()
        print(text)
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        # return HttpResponse("Your email sent")


    def resendEmailPasswordRecovery(self):
        pass

    def reset_password(self, user, request):
        c = {
            'email': user.email,
            'domain': request.META['HTTP_HOST'],
            'site_name': 'your site',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
            'token': default_token_generator.make_token(user),
            'protocol': 'http',
        }


        subject_template_name = 'registration/password_reset_subject.txt'

        email_template_name = 'registration/password_reset_email.html'

        subject = loader.render_to_string(subject_template_name, c)

        subject = ''.join(subject.splitlines())


        email = loader.render_to_string(email_template_name, c)

        print('The email is')
        print('emailbody:', email)
        print('------------')


        #send_mail(email_body, user.email)



    def post(self, request, *args, **kwargs):
        data = None
        form = self.form_class(request.POST)
        try:
            if form.is_valid():
                data = form.cleaned_data["email_or_username"]
                # print(data)
            if self.validate_email_address(data) is True:

                associated_users = User.objects.filter(
                    Q(email=data) | Q(username=data))


                if associated_users.exists():

                    for user in associated_users:

                        self.reset_password(user, request)

                    result = self.form_valid(form)

                    messages.success(
                        request, 'An email has been sent to {0}. Please check its inbox to continue reseting password.'.format(data))
                    return render(request, 'registration/EmailSend.html', {'email':data})
                    # return result
                result = self.form_invalid(form)
                messages.error(
                    request, 'No user is associated with this email address')
                # return HttpResponse('Email send')
                return HttpResponse('No user is associated with this email address')
            else:

                associated_users = User.objects.filter(username=data)
                if associated_users.exists():
                    for user in associated_users:
                        self.reset_password(user, request)
                    result = self.form_valid(form)
                    messages.success(
                        request, "Email has been sent to {0}'s email address. Please check its inbox to continue reseting password.".format(data))
                    return result
                result = self.form_invalid(form)
                messages.error(
                    request, 'This username does not exist in the system.')
                return result
            # messages.error(request, 'Invalid Input')
        except Exception as e:
            print(e)
        return self.form_invalid(form)


class PasswordResetConfirmView(FormView):
    template_name = "registration/password_reset_confirm.html"
    success_url = '/authentication/signin/'
    form_class = SetPasswordForm

    def post(self, request, uidb64=None, token=None, *arg, **kwargs):
        UserModel = get_user_model()
        form = self.form_class(request.POST)
        assert uidb64 is not None and token is not None  # checked by URLconf
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if form.is_valid():
                new_password = form.cleaned_data['new_password2']
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password has been reset.')
                return self.form_valid(form)
            else:
                messages.error(
                    request, 'Password reset has not been unsuccessful.')
                return self.form_invalid(form)
        else:
            messages.error(
                request, 'The reset password link is no longer valid.')
            return self.form_invalid(form)

# ------------------ ******  ------------------
