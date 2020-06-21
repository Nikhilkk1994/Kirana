from rest_framework import serializers as rest_serializers

from product import models as product_models


class CategorySerializer(rest_serializers.ModelSerializer):
    """
    Serializer for category
    """
    class Meta:
        model = product_models.Category
        fields = ('id', 'name', 'url',)


class ProductSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for Product
    """
    class Meta:
        model = product_models.Product
        fields = ('id', 'name', 'description',)


class ProductPersonalitySerializer(rest_serializers.ModelSerializer):
    """
    Serializer for Product Personality
    """
    class Meta:
        model = product_models.ProductPersonality
        fields = ('id', 'quantity', 'unit',)
