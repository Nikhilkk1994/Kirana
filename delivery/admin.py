from django.contrib import admin

from delivery import models as delivery_models

# Register your models here.
admin.site.register(delivery_models.Delivery)
