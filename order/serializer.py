from rest_framework import serializers as rest_serializers
from django.utils.translation import ugettext_lazy as _

from merchant import models as merchant_models


class CartCheckoutListSerializer(rest_serializers.ListSerializer):
    """
    Serializer for Cart Checkout
    """
    def validate(self, attrs):
        # validate the bulk objects at once
        attrs = list(set(attrs))
        # create the dict of the product
        product_dict = {}
        for data in attrs:
            key = ''.join([str(data[0]), str(data[1])])
            product_dict[key] = data[2]
        product = list(merchant_models.MerchantProductPersonality.objects.filter(
            merchant_product__in=[value[0] for value in attrs],
            product_personality__in=[value[1] for value in attrs],
            merchant_product__merchant=self.context.get('merchant_id'),
        ).values('inventory', 'merchant_product_id', 'product_personality_id'))
        # validate the product Inventory
        count = 0
        for data in product:
            key = ''.join([str(data['merchant_product_id']), str(data['product_personality_id'])])
            if product_dict.get(key, None):
                if product_dict[key] <= data['inventory']:
                    data['inventory'] = product_dict[key]
            else:
                product.pop(count)
            count = count + 1
        return product


class CartCheckoutSerializer(rest_serializers.Serializer):
    """
    Serializer for Cart Checkout
    """
    merchant_product_id = rest_serializers.IntegerField(required=True, label=_('Merchant Product ID'))
    inventory = rest_serializers.IntegerField(required=True, label=_('Inventory of the Product'))
    product_personality_id = rest_serializers.IntegerField(required=True, label=_('Product Personality ID'))

    class Meta:
        list_serializer_class = CartCheckoutListSerializer

    def validate(self, attrs):
        # validate the single object
        return (
            attrs.get('merchant_product_id', None), attrs.get('product_personality_id', None),
            attrs.get('inventory', 0)
        )
