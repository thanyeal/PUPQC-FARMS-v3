from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager  # Import BaseUserManager
from django.utils import timezone
from django.contrib.auth.models import AnonymousUser
from werkzeug.security import generate_password_hash

# Create your models here.
class FISFaculty(models.Model): # Inherit from the abstract base user and permissions mixin
    FacultyId = models.AutoField(primary_key=True)
    FacultyType = models.CharField(max_length=50)
    Rank = models.CharField(max_length=50, blank=True, null=True)  # Assuming Rank is optional
    Units = models.FloatField()
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50, blank=True, null=True)
    MiddleInitial = models.CharField(max_length=50, blank=True, null=True)
    NameExtension = models.CharField(max_length=50, blank=True, null=True)
    BirthDate = models.DateField()
    DateHired = models.DateField()
    Degree = models.TextField(blank=True, null=True)  # Changed to TextField for flexibility
    Remarks = models.TextField(blank=True, null=True)
    FacultyCode = models.IntegerField()  # Faculty Code
    Honorific = models.CharField(max_length=50, blank=True, null=True)
    Age = models.IntegerField()  # Changed to IntegerField
    Specialization = models.CharField(max_length=255, blank=True, null=True)  # Set max_length 
    PreferredSchedule = models.CharField(max_length=255, blank=True, null=True)

    Email = models.EmailField(unique=True)  # Use EmailField for validation
    ResidentialAddress = models.CharField(max_length=255, blank=True, null=True)
    MobileNumber = models.CharField(max_length=11, blank=True, null=True) # Add max_length
    Gender = models.IntegerField(choices=((1, "Male"), (2, "Female")), blank=True, null=True)  # Add choices

    Password = models.CharField(max_length=256)
    ProfilePic = models.ImageField(upload_to='profile_pics/', default='default.png')  # Use ImageField and add upload_to
    Status = models.CharField(max_length=50, default='Deactivated')
    Login_Attempt = models.IntegerField(default=12)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')


    def __str__(self):
        return self.Email  # or a more user-friendly representation
    class Meta():
        db_table = 'FISFaculty' 
        managed = False  

    @property  # Make it a read-only property
    def is_authenticated(self):
        return True



class CustomAccountManager(BaseUserManager):

    def create_superuser(self, Email, FirstName, MiddleName , LastName, password,  **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(Email, FirstName, MiddleName , LastName, password, **other_fields)

    def create_user(self, Email, FirstName, MiddleName , LastName ,password, **other_fields):

        if not Email:
            raise ValueError(_('You must provide an Email address'))

        Email = self.normalize_email(Email)
        user = self.model(Email=Email,
                          FirstName=FirstName, MiddleName=MiddleName , LastName=LastName,**other_fields)
        user.password =  generate_password_hash(password, method='pbkdf2', salt_length=16)
        user.save()
        return user

    

# Create your models here.
class FARMSUser(AbstractBaseUser, PermissionsMixin): # Inherit from the abstract base user and permissions mixin
    UserId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50, blank=True, null=True)
    MiddleInitial = models.CharField(max_length=50, blank=True, null=True)
    NameExtension = models.CharField(max_length=50, blank=True, null=True)
    BirthDate = models.DateField(blank=True, null=True)
    DateHired = models.DateField(blank=True, null=True)
    Honorific = models.CharField(max_length=50, blank=True, null=True)
    Age = models.IntegerField(blank=True, null=True)  # Changed to IntegerField
    Email = models.EmailField(unique=True)  # Use EmailField for validation
    ResidentialAddress = models.CharField(max_length=255, blank=True, null=True)
    MobileNumber = models.CharField(max_length=11, blank=True, null=True) # Add max_length
    Gender = models.IntegerField(choices=((1, "Male"), (2, "Female")), blank=True, null=True)  # Add choices
    ProfilePic = models.ImageField(upload_to='profile_pics/', default='default.png')  # Use ImageField and add upload_to
    Status = models.CharField(max_length=50, default='Deactivated')
    Login_Attempt = models.IntegerField(default=12)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='created_user', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='modified_user', null=True, blank=True)
    created_by_faculty = models.ForeignKey(settings.AUTH_FACULTY_MODEL, on_delete=models.PROTECT, related_name='created_faculty_user', null=True, blank=True)
    modified_by_faculty = models.ForeignKey( settings.AUTH_FACULTY_MODEL, on_delete=models.PROTECT, related_name='modified_faculty_user', null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'Email'  # Make Email as the authentication field
    REQUIRED_FIELDS = ['FirstName', 'LastName', 'MiddleName']

    objects = CustomAccountManager()

    def __str__(self):
        return self.Email  # or a more user-friendly representation
    
    class Meta():
        db_table = 'FARMSUser' 


    