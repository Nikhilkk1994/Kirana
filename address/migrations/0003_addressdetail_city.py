# Generated by Django 2.0 on 2020-09-19 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20200616_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressdetail',
            name='city',
            field=models.TextField(default='city', max_length=30, verbose_name='City'),
            preserve_default=False,
        ),
    ]
