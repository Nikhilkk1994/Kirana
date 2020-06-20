from django.contrib import admin

from merchant import models as merchant_models

# Register your models here.
admin.site.register(merchant_models.Merchant)
admin.site.register(merchant_models.MerchantProducts)
