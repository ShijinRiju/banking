# Generated by Django 5.0.4 on 2024-04-22 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0015_complaints'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bankingapp.register'),
        ),
    ]
