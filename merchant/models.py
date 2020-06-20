from django.db import models
from django.utils.translation import ugettext_lazy as _

from customer import models as customer_models
from customer.model_validator import validate_mobile
from address import models as address_models


class Merchant(models.Model):
    """
    Merchant model
    """
    owner = models.OneToOneField(customer_models.User, on_delete=models.CASCADE)
    store_name = models.CharField(_('Store Name'), max_length=50, unique=True)
    mobile = models.IntegerField(_('Mobile Number of Shop'), validators=[validate_mobile])
    address = models.OneToOneField(address_models.Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Merchant')
        verbose_name_plural = _('Merchants')

    def __str__(self):
        return self.store_name
