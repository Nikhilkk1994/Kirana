from django.contrib import admin

from address.models import Address, AddressDetail

# Register your models here.
admin.site.register(Address)
admin.site.register(AddressDetail)