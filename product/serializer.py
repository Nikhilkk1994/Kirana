from rest_framework import serializers as rest_serializers

from product import models as product_models


class CategorySerializer(rest_serializers.ModelSerializer):
    """
    Serializer for category
    """
    class Meta:
        model = product_models.Category
        fields = ('id', 'name', 'url', 'description',)


class ProductSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for Product
    """
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = product_models.Product
        fields = ('id', 'name', 'description', 'category',)


class ProductPersonalitySerializer(rest_serializers.ModelSerializer):
    """
    Serializer for Product Personality
    """
    class Meta:
        model = product_models.ProductPersonality
        fields = ('id', 'quantity', 'unit',)
