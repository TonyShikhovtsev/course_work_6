# Generated by Django 4.2.3 on 2023-12-09 03:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blog_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 9, 6, 52, 44, 378011), verbose_name='Дата создания'),
        ),
    ]