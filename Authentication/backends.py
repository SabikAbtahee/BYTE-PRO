import Database

class CustomUserAuth(object):

    def authenticate(self, username=None, password=None):
        try:
            user = Database.models.customUser.objects.get(email=username)
            if user.check_password(password):
                return user
        except Database.models.customUser.DoesNotExist:
            return None

    def get_user(self,user_id):
        try:
            user = Database.models.customUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None

        except Database.models.customUser.DoesNotExist:
            return None