from django.db import models
from django.utils.translation import ugettext_lazy as _

from customer import models as customer_models
from customer.model_validator import validate_mobile
from address import models as address_models
from product import models as product_models


class Merchant(models.Model):
    """
    Merchant model
    """
    owner = models.OneToOneField(customer_models.User, on_delete=models.CASCADE)
    store_name = models.CharField(_('Store Name'), max_length=50, unique=True)
    mobile = models.BigIntegerField(_('Mobile Number of Shop'), validators=[validate_mobile])
    address = models.OneToOneField(address_models.Address, on_delete=models.CASCADE)
    serve_zip_code = models.ManyToManyField(address_models.AddressDetail, related_name='merchants', blank=True)
    image = models.ImageField(max_length=255, upload_to='media/merchant/', blank=True, null=True)

    class Meta:
        verbose_name = _('Merchant')
        verbose_name_plural = _('Merchants')

    def __str__(self):
        return self.store_name


class MerchantProducts(models.Model):
    """
    Merchant Products
    """
    product = models.ForeignKey(product_models.Product, on_delete=models.CASCADE)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    max_quantity = models.IntegerField(_('Max quantity can added to cart'), blank=True, null=True)

    class Meta:
        verbose_name = _('Merchant Product')
        verbose_name_plural = _('Merchant Products')
        unique_together = ('product', 'merchant',)

    def __str__(self):
        return self.product.name + ' ' + self.merchant.store_name


class MerchantProductPersonality(models.Model):
    """
    Model for Merchant Product Personality
    """
    merchant_product = models.ForeignKey(MerchantProducts, on_delete=models.CASCADE)
    product_personality = models.ForeignKey(product_models.ProductPersonality, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(_('Price of Product'))
    inventory = models.PositiveIntegerField(_('Inventory of Product'))

    class Meta:
        verbose_name = _('Merchant Product Personality')
        verbose_name_plural = _('Merchant Products Personality')
        unique_together = ('merchant_product', 'product_personality',)

    def __str__(self):
        return self.merchant_product.product.name + ' ' + self.merchant_product.merchant.store_name
