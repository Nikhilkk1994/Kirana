# Generated by Django 3.0.7 on 2020-06-16 04:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20200616_0433'),
        ('customer', '0004_auto_20200614_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.ManyToManyField(blank=True, related_name='address', through='customer.UserToAddress', to='address.Address'),
        ),
    ]