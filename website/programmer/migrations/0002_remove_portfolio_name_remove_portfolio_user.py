# Generated by Django 4.2.4 on 2023-09-11 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programmer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='name',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='user',
        ),
    ]
