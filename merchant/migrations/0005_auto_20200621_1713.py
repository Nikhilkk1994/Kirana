# Generated by Django 3.0.7 on 2020-06-21 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200620_1136'),
        ('merchant', '0004_auto_20200621_1652'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='merchantproducts',
            unique_together={('product', 'merchant')},
        ),
    ]
