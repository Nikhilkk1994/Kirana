from rest_framework import serializers as rest_serializers
from django.utils.translation import ugettext_lazy as _

from merchant import models as merchant_models
from customer import models as customer_models
from address import serializer as address_serializer
from product import serializer as product_serializer


class CartCheckoutListSerializer(rest_serializers.ListSerializer):
    """
    Serializer for Cart Checkout
    """
    def validate(self, attrs):
        # validate the bulk objects at once
        return attrs


class CartCheckoutSerializer(rest_serializers.Serializer):
    """
    Serializer for Cart Checkout
    """
    merchant_product_id = rest_serializers.IntegerField(required=False, label=_('Merchant Product ID'))
    inventory = rest_serializers.IntegerField(required=False, label=_('Inventory of the Product'))
    product_personality_id = rest_serializers.IntegerField(required=False, label=_('Product Personality ID'))
    status = rest_serializers.CharField(required=False, label=_('Error Message'), default='')

    class Meta:
        list_serializer_class = CartCheckoutListSerializer

    def validate(self, attrs):
        # validate the single object
        return self.validate_all_required_fields(attrs)

    def validate_all_required_fields(self, data):
        """
        Verify that this object have all required field
        """
        result = []
        if not data.get('merchant_product_id', None):
            result.append('merchant_product_id')
        if not data.get('inventory', None):
            result.append('inventory')
        if not data.get('product_personality_id', None):
            result.append('product_personality_id')
        if len(result):
            return {'status': 'error, here are list of fields that are required {} '.format(', '.join(result))}
        return data
