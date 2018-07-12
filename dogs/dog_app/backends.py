from .models import MyUser
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            User = get_user_model()

            user = User.objects.get(email=username)
        except User.MultipleObjectsReturned:
            user = User.objects.filter(email=username).order_by('id').first()

        except User.DoesNotExist:
            return None

        if getattr(user, 'is_active') and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            User = get_user_model()
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class MobileBackend(ModelBackend):

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            User = get_user_model()
            user = User.objects.get(contact=username)
        except User.MultipleObjectsReturned:
            user = User.objects.filter(contact=username).order_by('id').first()

        except User.DoesNotExist:
            return None

        if getattr(user, 'is_active') and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            User = get_user_model()
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


