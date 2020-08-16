# Generated by Django 3.0.7 on 2020-08-16 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Product Keyword')),
            ],
            options={
                'verbose_name': 'Product Keyword',
                'verbose_name_plural': 'Product Keywords',
            },
        ),
    ]
