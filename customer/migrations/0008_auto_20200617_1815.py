# Generated by Django 3.0.7 on 2020-06-17 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20200616_0433'),
        ('customer', '0007_auto_20200616_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.ManyToManyField(blank=True, related_name='user', through='customer.UserToAddress', to='address.Address'),
        ),
    ]
