from django.contrib.auth.backends import ModelBackend
from .models import Farmer

class FarmerBackend(ModelBackend):
    print(f"****Somebody callle the farmer backend")
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(f"****Somebody callle the farmer backend")
        try:
            print(f"****Somebody callle the farmer backend and passed the username {username} and password {password}")
            user = Farmer.objects.get(username=username)
            print(f"****the returned user object is {user}")
                # print(f"*** WE got the following user {user}")
            return user
        except Farmer.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return Farmer.objects.get(pk=user_id)
        except Farmer.DoesNotExist:
            return None
