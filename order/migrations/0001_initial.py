# Generated by Django 3.0.7 on 2020-06-20 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('merchant', '0003_merchantproductpersonality'),
        ('delivery', '0001_initial'),
        ('address', '0002_auto_20200616_0433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_to_merchant', models.IntegerField(choices=[(1, 'Payment Pending'), (2, 'Payment Done')], db_index=True, default=1, verbose_name='Payment To Merchant')),
                ('payment_type', models.IntegerField(choices=[(1, 'Cash On Delivery'), (2, 'Online Payment')], db_index=True, default=1, verbose_name='Payment Type')),
                ('status', models.IntegerField(choices=[(1, 'Pending Verification'), (2, 'Order Accepted'), (3, 'Order Ready to Pick Up'), (4, 'Order Dispatched'), (5, 'Order Delivered'), (6, 'Order Cancelled')], db_index=True, default=1, verbose_name='Order Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Order Created At')),
                ('delivered_at', models.DateTimeField(auto_now_add=True, help_text='Order Deliverd At')),
                ('ready_at', models.DateTimeField(auto_now_add=True, help_text='Order Ready At')),
                ('accepted_at', models.DateTimeField(auto_now_add=True, help_text='Order Accepted At')),
                ('dispatched_at', models.DateTimeField(auto_now_add=True, help_text='Order Dispatched At')),
                ('cancelled_at', models.DateTimeField(auto_now_add=True, help_text='Order Cancelled At')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.Address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('delivery_agent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.Delivery')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant.Merchant')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
