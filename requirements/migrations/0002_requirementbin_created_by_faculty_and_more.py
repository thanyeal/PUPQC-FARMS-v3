# Generated by Django 5.0.6 on 2024-06-02 10:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('requirements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirementbin',
            name='created_by_faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_faculty_requirementbin', to='accounts.fisfaculty'),
        ),
        migrations.AddField(
            model_name='requirementbin',
            name='modified_by_faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modified_faculty_requirementbin', to='accounts.fisfaculty'),
        ),
        migrations.AddField(
            model_name='requirementbincontent',
            name='created_by_faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_faculty_reqcontent', to='accounts.fisfaculty'),
        ),
        migrations.AddField(
            model_name='requirementbincontent',
            name='modified_by_faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modified_faculty_reqcontent', to='accounts.fisfaculty'),
        ),
        migrations.AddField(
            model_name='userrequirementupload',
            name='assigned_by_faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assignedby_faculty_UserRequirementUpload', to='accounts.fisfaculty'),
        ),
        migrations.AddField(
            model_name='userrequirementupload',
            name='assigned_to_faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assignedto_faculty_UserRequirementUpload', to='accounts.fisfaculty'),
        ),
        migrations.AddField(
            model_name='userrequirementupload',
            name='created_by_faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='createdby_faculty_UserRequirementUpload', to='accounts.fisfaculty'),
        ),
        migrations.AddField(
            model_name='userrequirementupload',
            name='modified_by_faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modifiedby_faculty_UserRequirementUpload', to='accounts.fisfaculty'),
        ),
        migrations.AddField(
            model_name='userrequirementupload',
            name='reviewed_by_faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reviewedby_faculty_UserRequirementUpload', to='accounts.fisfaculty'),
        ),
    ]