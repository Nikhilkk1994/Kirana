# Generated by Django 3.0.7 on 2020-07-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
