# Generated by Django 4.2.3 on 2023-12-08 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='message',
            field=models.CharField(default=None, max_length=255, verbose_name='Сообщение'),
        ),
    ]
