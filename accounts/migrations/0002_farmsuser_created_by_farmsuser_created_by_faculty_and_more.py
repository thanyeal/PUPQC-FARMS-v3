# Generated by Django 5.0.6 on 2024-06-02 10:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmsuser',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='farmsuser',
            name='created_by_faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_faculty_user', to='accounts.fisfaculty'),
        ),
        migrations.AddField(
            model_name='farmsuser',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modified_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='farmsuser',
            name='modified_by_faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modified_faculty_user', to='accounts.fisfaculty'),
        ),
    ]
