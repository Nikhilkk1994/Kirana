# Generated by Django 3.0.7 on 2020-06-14 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20200614_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.PositiveIntegerField(unique=True, verbose_name='mobile number'),
        ),
    ]
