# Generated by Django 4.1.3 on 2022-11-30 14:12
import os

from django.contrib.auth import get_user_model
from django.db import migrations


def create_superuser(apps, schema_editor):
    # Account = apps.get_model('users', 'Account')
    Account = get_user_model()

    DJ_SU_FULLNAME = os.environ.get('DJ_SU_FULLNAME')
    DJ_SU_EMAIL = os.environ.get('DJ_SU_EMAIL')
    DJ_SU_PASSWORD = os.environ.get('DJ_SU_PASSWORD')

    Account.objects.create_superuser(
        email=DJ_SU_EMAIL,
        fullname=DJ_SU_FULLNAME,
        password=DJ_SU_PASSWORD
    )


def delete_superuser(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0003_groups'),
    ]

    operations = [
        migrations.RunPython(create_superuser, delete_superuser)
    ]