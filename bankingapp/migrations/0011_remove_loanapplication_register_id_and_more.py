# Generated by Django 5.0.4 on 2024-04-17 13:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0010_remove_loanapplication_login_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanapplication',
            name='register_id',
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='login_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
