# Generated by Django 4.2.3 on 2023-12-08 20:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 23, 7, 5, 312488), verbose_name='Дата создания'),
        ),
    ]
