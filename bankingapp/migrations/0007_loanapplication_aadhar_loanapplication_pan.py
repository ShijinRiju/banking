# Generated by Django 5.0.4 on 2024-04-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0006_loanapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanapplication',
            name='aadhar',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='pan',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
