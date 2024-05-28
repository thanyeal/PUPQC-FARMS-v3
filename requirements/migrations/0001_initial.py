# Generated by Django 5.0.6 on 2024-05-28 03:54

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utilities', '0007_rename_category_id_requirementtype_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequirementBin',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('deadline', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('has_child_records', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sy_semester', to='utilities.requirementcategory')),
            ],
            options={
                'db_table': 'FARMSRequirementBin',
                'unique_together': {('name', 'category')},
            },
        ),
    ]