from django.db import models
import uuid

# Create your models here.
class SchoolYear(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, unique=True) 
    start_date = models.DateField()
    end_date = models.DateField()
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='created_program_accreditation', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    # modified_by = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='modified_program_accreditation', null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=False, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    
    class Meta:
        db_table = 'FARMSSchoolYear'

    def __str__(self):
        return(self.name) 



# Create your models here.
class Semester(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school_year = models.ForeignKey(SchoolYear, on_delete=models.PROTECT, related_name='sy_semester', null=True, blank=True)
    name = models.CharField(max_length=150) 
    start_date = models.DateField()
    end_date = models.DateField()
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='created_program_accreditation', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    # modified_by = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='modified_program_accreditation', null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=False, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    
    class Meta:
        db_table = 'FARMSSemester' 
        unique_together = ('name', 'school_year')
