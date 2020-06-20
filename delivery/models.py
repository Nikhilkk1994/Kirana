from django.db import models
from django.utils.translation import ugettext_lazy as _

from customer import models as customer_models
from address import models as address_models


class Delivery(models.Model):
    """
    Model for Delivery Agent
    """
    delivery = models.OneToOneField(customer_models.User, on_delete=models.CASCADE)
    address = models.ForeignKey(address_models.Address, on_delete=models.CASCADE)
    detail = models.CharField(_('Delivery Agent Details'), max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _('Delivery Agent')
        verbose_name_plural = _('Delivery Agents')

    def __str__(self):
        return str(self.delivery.mobile)
