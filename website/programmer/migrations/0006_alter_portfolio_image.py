# Generated by Django 4.2.4 on 2023-09-17 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmer', '0005_alter_portfolio_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
