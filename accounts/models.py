from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager  # Import BaseUserManager
from django.utils import timezone

# Create your models here.
class FISFaculty(AbstractBaseUser, PermissionsMixin): # Inherit from the abstract base user and permissions mixin
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

    USERNAME_FIELD = 'email'  # Make Email as the authentication field
    # REQUIRED_FIELDS = []  # You might want to add REQUIRED_FIELDS if needed
    # objects = FISFacultyManager()  # Use the custom user manager

    def __str__(self):
        return self.email  # or a more user-friendly representation
    

    