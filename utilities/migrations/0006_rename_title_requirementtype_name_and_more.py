# Generated by Django 5.0.6 on 2024-05-27 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0005_requirementcategory_has_child_records_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requirementtype',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterUniqueTogether(
            name='requirementcategory',
            unique_together={('title', 'semester')},
        ),
    ]