from django.db import models
from django.utils.translation import ugettext_lazy as _


class AddressDetail(models.Model):
    city = models.CharField(_('City'), max_length=30)
    state = models.CharField(_('State'), max_length=30)
    country = models.CharField(_('Country'), max_length=30)
    zip_code = models.CharField(_('Zip Code'), max_length=30)

    class Meta:
        verbose_name = _('Address Detail')
        verbose_name_plural = _('Address Details')

    def __str__(self):
        return self.zip_code


class Address(models.Model):
    """
    Model for the Address for customer/merchant/delivery Agent
    """
    area_house_number = models.CharField(_('Area detail and House Number'), max_length=50)
    landmark = models.CharField(_('Landmark'), max_length=50, blank=True, null=True)
    address_detail = models.ForeignKey(AddressDetail, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Address')

    def __str__(self):
        return self.area_house_number
