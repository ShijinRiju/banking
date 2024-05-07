# Generated by Django 5.0.4 on 2024-04-11 06:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0003_deposits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposits',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankingapp.register'),
        ),
        migrations.AlterField(
            model_name='deposits',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]