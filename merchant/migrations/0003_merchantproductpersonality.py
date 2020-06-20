# Generated by Django 3.0.7 on 2020-06-20 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200620_1136'),
        ('merchant', '0002_merchantproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='MerchantProductPersonality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='Price of Product')),
                ('inventory', models.PositiveIntegerField(verbose_name='Inventory of Product')),
                ('merchant_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant.MerchantProducts')),
                ('product_personality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductPersonality')),
            ],
            options={
                'verbose_name': 'Merchant Product Personality',
                'verbose_name_plural': 'Merchant Products Personality',
            },
        ),
    ]
