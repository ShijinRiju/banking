# Generated by Django 5.0.4 on 2024-04-17 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0011_remove_loanapplication_register_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanapplication',
            name='login_id',
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='register_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bankingapp.register'),
        ),
    ]
