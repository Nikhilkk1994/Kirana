# Generated by Django 2.0 on 2020-09-19 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_addressdetail_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressdetail',
            name='city',
            field=models.CharField(max_length=30, verbose_name='City'),
        ),
    ]
