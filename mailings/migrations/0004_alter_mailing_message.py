# Generated by Django 4.2.3 on 2023-12-08 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0003_alter_mailing_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.message', verbose_name='Сообщение'),
        ),
    ]