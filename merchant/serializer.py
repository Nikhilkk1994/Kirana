from rest_framework import serializers as rest_serializers

from merchant import models as merchant_models
from customer import models as customer_models
from address import serializer as address_serializer
from product import serializer as product_serializer


class BaseUserSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for user(customer, ect)
    """
    class Meta:
        model = customer_models.User
        fields = ('id', 'mobile', 'first_name', 'last_name',)


class MerchantSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for category
    """
    owner = BaseUserSerializer(read_only=True)
    address = address_serializer.UserAddressSerializer(read_only=True)

    class Meta:
        model = merchant_models.Merchant
        fields = ('id', 'store_name', 'mobile', 'address', 'owner',)


class MerchantProductPersonalitySerializer(rest_serializers.ModelSerializer):
    """
    Serializer for Merchant Product Serializer
    """
    product_personality = product_serializer.ProductPersonalitySerializer()

    class Meta:
        model = merchant_models.MerchantProductPersonality
        fields = ('price', 'inventory', 'product_personality',)


class MerchantProductSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for Merchant ProductMer Serializer
    """
    product = product_serializer.ProductSerializer()
    configuration = MerchantProductPersonalitySerializer(source="merchantproductpersonality_set", many=True)

    class Meta:
        model = merchant_models.MerchantProducts
        fields = ('id', 'max_quantity', 'product', 'configuration',)
