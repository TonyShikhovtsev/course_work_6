# Generated by Django 4.2.3 on 2023-12-07 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 7, 22, 37, 21, 447415), verbose_name='Дата создания'),
        ),
    ]
