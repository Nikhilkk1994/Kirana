from rest_framework import serializers as rest_serializers

from merchant import models as merchant_models
from customer import models as customer_models
from address import serializer as address_serializer


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
