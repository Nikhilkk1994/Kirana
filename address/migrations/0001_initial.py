# Generated by Django 3.0.7 on 2020-06-16 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_house_number', models.CharField(max_length=50, verbose_name='Area detail and House Number')),
                ('state', models.CharField(max_length=30, verbose_name='State')),
                ('country', models.CharField(max_length=30, verbose_name='Country')),
                ('zip_code', models.CharField(max_length=30, verbose_name='Zip Code')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Address',
            },
        ),
    ]