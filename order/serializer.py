from rest_framework import serializers as rest_serializers
from django.utils.translation import ugettext_lazy as _

from merchant import models as merchant_models


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
    status = rest_serializers.CharField(required=False, label=_('Error Status'), default='')
    message = rest_serializers.CharField(required=False, label=_('ATC message'), default='')

    class Meta:
        list_serializer_class = CartCheckoutListSerializer

    def validate(self, attrs):
        # validate the single object
        attrs = self.validate_all_required_fields(attrs)
        if attrs.get('status') == 200:
            # verify the product is available and belong to same merchant
            product = merchant_models.MerchantProductPersonality.objects.filter(
                merchant_product=attrs.get('merchant_product_id'),
                product_personality=attrs.get('product_personality_id'),
                merchant_product__merchant=self.context.get('merchant_id')
            )
            if product.exists():
                if attrs.get('inventory') > product.first().inventory:
                    attrs['message'] = 'Product is in shortage, decrease the inventory to {}'.format(
                        product.first().inventory
                    )
                    attrs['inventory'] = product.first().inventory
                    if attrs['inventory'] == 0:
                        attrs['status'] = 404
                        attrs['message'] = 'Out Of Stock'
            else:
                attrs['status'] = 404
                attrs['message'] = 'Product not exists, Not belong to merchant with ID {}'.format(
                    self.context.get('merchant_id')
                )
        return attrs

    def validate_all_required_fields(self, data):
        """
        Verify that object have all required field
        """
        result = []
        if not data.get('merchant_product_id', None):
            result.append('merchant_product_id')
        if not data.get('inventory', None):
            result.append('inventory')
        if not data.get('product_personality_id', None):
            result.append('product_personality_id')
        if len(result):
            data['status'], data['message'] = (
                400, 'error, here are list of fields that are required {} '.format(', '.join(result))
            )
            return data
        data['status'], data['message'] = 200, 'Add To Cart check success'
        return data
