# Generated by Django 5.0.7 on 2024-07-21 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Article',
        ),
    ]
