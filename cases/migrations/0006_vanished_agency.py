# Generated by Django 3.1.7 on 2021-02-23 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0005_auto_20210223_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='vanished',
            name='agency',
            field=models.TextField(blank=True),
        ),
    ]
