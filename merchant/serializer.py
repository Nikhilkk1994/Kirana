from rest_framework import serializers as rest_serializers

from merchant import models as merchant_models
from customer import models as customer_models
from product import models as product_models
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
        fields = ('product_personality', 'price', 'inventory',)


class MerchantProductSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for Merchant Product Serializer
    """
    product = product_serializer.ProductSerializer()
    configuration = rest_serializers.SerializerMethodField()

    class Meta:
        model = merchant_models.MerchantProducts
        fields = ('id', 'product', 'configuration',)

    def get_configuration(self, instance):
        queryset = merchant_models.MerchantProductPersonality.objects.filter(merchant_product__id=instance.id)
        return MerchantProductPersonalitySerializer(queryset, many=True).data


class MerchantMenuSerializer(rest_serializers.Serializer):
    """
    Serializer for Merchant Product
    """
    products = rest_serializers.SerializerMethodField()

    class Meta:
        model = merchant_models.Merchant
        fields = ('products',)

    def get_products(self, instance):
        queryset = merchant_models.MerchantProducts.objects.filter(merchant__id=instance.id)
        return MerchantProductSerializer(queryset, many=True).data
