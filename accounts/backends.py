# your_app/backends.py  (Create a new file named "backends.py" in your app)

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from accounts.models import FARMSUser, FISFaculty       
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash  

class MultiTableAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Determine which table to authenticate against
        try:
            user = FARMSUser.objects.get(Email=username) 
            # Check password
            if check_password_hash(user.password, password): 
                return user
        except FARMSUser.DoesNotExist:
            try:
                user = FISFaculty.objects.get(Email=username)                 
                if check_password_hash(user.Password, password): 
                    return user
            except FISFaculty.DoesNotExist:
                return None 

        return None  # Authentication failed

    def get_user(self, user_id):
        try:
            return FARMSUser.objects.get(pk=user_id)  # Try to fetch from FARMSUser first
        except FARMSUser.DoesNotExist:
            try:
                return FISFaculty.objects.get(FacultyId=user_id)  # Try FISFaculty if not found
            except FISFaculty.DoesNotExist:
                return None
