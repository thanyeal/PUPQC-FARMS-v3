from django.db import models

from utilities.models import RequirementCategory
import uuid


# Create your models here.
class RequirementBin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(RequirementCategory, on_delete=models.PROTECT, related_name='category_requirementbin', null=True, blank=True)
    name = models.CharField(max_length=2000) 
    deadline = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20) 
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='created_program_accreditation', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    # modified_by = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='modified_program_accreditation', null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=False, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    has_child_records = models.BooleanField(default=False)

    
    class Meta:
        db_table = 'FARMSRequirementBin' 
        unique_together = ('name', 'category')

    # def __str__(self):
    #     return '%s %s' % ('S.Y. ' + self.school_year.name, '- ' + self.name)