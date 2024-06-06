# Generated by Django 5.0.6 on 2024-06-01 16:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='FISFaculty',
            fields=[
                ('FacultyId', models.AutoField(primary_key=True, serialize=False)),
                ('FacultyType', models.CharField(max_length=50)),
                ('Rank', models.CharField(blank=True, max_length=50, null=True)),
                ('Units', models.FloatField()),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('MiddleName', models.CharField(blank=True, max_length=50, null=True)),
                ('MiddleInitial', models.CharField(blank=True, max_length=50, null=True)),
                ('NameExtension', models.CharField(blank=True, max_length=50, null=True)),
                ('BirthDate', models.DateField()),
                ('DateHired', models.DateField()),
                ('Degree', models.TextField(blank=True, null=True)),
                ('Remarks', models.TextField(blank=True, null=True)),
                ('FacultyCode', models.IntegerField()),
                ('Honorific', models.CharField(blank=True, max_length=50, null=True)),
                ('Age', models.IntegerField()),
                ('Specialization', models.CharField(blank=True, max_length=255, null=True)),
                ('PreferredSchedule', models.CharField(blank=True, max_length=255, null=True)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('ResidentialAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('MobileNumber', models.CharField(blank=True, max_length=11, null=True)),
                ('Gender', models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True)),
                ('Password', models.CharField(max_length=256)),
                ('ProfilePic', models.ImageField(default='default.png', upload_to='profile_pics/')),
                ('Status', models.CharField(default='Deactivated', max_length=50)),
                ('Login_Attempt', models.IntegerField(default=12)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'FISFaculty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FARMSUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('MiddleName', models.CharField(blank=True, max_length=50, null=True)),
                ('MiddleInitial', models.CharField(blank=True, max_length=50, null=True)),
                ('NameExtension', models.CharField(blank=True, max_length=50, null=True)),
                ('BirthDate', models.DateField(blank=True, null=True)),
                ('DateHired', models.DateField(blank=True, null=True)),
                ('Honorific', models.CharField(blank=True, max_length=50, null=True)),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('ResidentialAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('MobileNumber', models.CharField(blank=True, max_length=11, null=True)),
                ('Gender', models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True)),
                ('ProfilePic', models.ImageField(default='default.png', upload_to='profile_pics/')),
                ('Status', models.CharField(default='Deactivated', max_length=50)),
                ('Login_Attempt', models.IntegerField(default=12)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'FARMSUser',
            },
        ),
    ]