from django.db import models
from django.utils.translation import ugettext_lazy as _

from customer import models as customer_models
from merchant import models as merchant_models
from product import models as product_models
from delivery import models as delivery_models
from address import models as address_models


class Order(models.Model):
    """
    Model for the Order
    """
    PENDING, COMPLETE = 1, 2
    COD, ONLINE = 1, 2
    PENDING_VERIFY, ACCEPTED, READY, DISPATCHED, DELIVERED, CANCELLED = 1, 2, 3, 4, 5, 6
    _PAYMENT_STATUS = (
        (PENDING, _('Payment Pending')),
        (COMPLETE, _('Payment Done'))
    )
    _PAYMENT_TYPE = (
        (COD, _('Cash On Delivery')),
        (ONLINE, _('Online Payment'))
    )
    _ORDER_STATUS = (
        (PENDING_VERIFY, _('Pending Verification')),
        (ACCEPTED, _('Order Accepted')),
        (READY, _('Order Ready to Pick Up')),
        (DISPATCHED, _('Order Dispatched')),
        (DELIVERED, _('Order Delivered')),
        (CANCELLED, _('Order Cancelled'))
    )
    customer = models.ForeignKey(customer_models.User, on_delete=models.CASCADE)
    merchant = models.ForeignKey(merchant_models.Merchant, on_delete=models.CASCADE)
    address = models.ForeignKey(address_models.Address, on_delete=models.CASCADE)
    delivery_agent = models.ForeignKey(delivery_models.Delivery, on_delete=models.CASCADE, blank=True, null=True)
    payment_to_merchant = models.IntegerField(
        choices=_PAYMENT_STATUS, default=PENDING, verbose_name=_('Payment To Merchant'), db_index=True
    )
    payment_type = models.IntegerField(
        choices=_PAYMENT_TYPE, default=COD, verbose_name=_('Payment Type'), db_index=True
    )
    status = models.IntegerField(
        choices=_ORDER_STATUS, default=PENDING_VERIFY, verbose_name=_('Order Status'), db_index=True
    )
    created_at = models.DateTimeField(help_text=_('Order Created At'), auto_now_add=True)
    delivered_at = models.DateTimeField(help_text=_('Order Deliverd At'), auto_now_add=True)
    ready_at = models.DateTimeField(help_text=_('Order Ready At'), auto_now_add=True)
    accepted_at = models.DateTimeField(help_text=_('Order Accepted At'), auto_now_add=True)
    dispatched_at = models.DateTimeField(help_text=_('Order Dispatched At'), auto_now_add=True)
    cancelled_at = models.DateTimeField(help_text=_('Order Cancelled At'), auto_now_add=True)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return str(self.customer.mobile) + ' ' + self.merchant.store_name


class OrderProducts(models.Model):
    """
    Model for Order to Product Cart
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    merchant_products = models.ForeignKey(merchant_models.MerchantProducts, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_('Quantity of product'))

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    def __str__(self):
        return 'Order ID: ' + str(self.order.id) + ' ' + 'merchant: ' + self.merchant_products.merchant.store_name
