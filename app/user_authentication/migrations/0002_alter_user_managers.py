# Generated by Django 4.1.4 on 2023-05-25 15:06

import app.user_authentication.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', app.user_authentication.models.CustomUserManager()),
            ],
        ),
    ]
