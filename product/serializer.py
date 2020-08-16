from rest_framework import serializers as rest_serializers

from product import models as product_models


class CategorySerializer(rest_serializers.ModelSerializer):
    """
    Serializer for category
    """
    image = rest_serializers.SerializerMethodField()

    class Meta:
        model = product_models.Category
        fields = ('id', 'name', 'url', 'description', 'image',)

    def get_image(self, instance):
        if instance.image:
            return instance.image.url
        return None


class ProductSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for Product
    """
    category = CategorySerializer(many=True, read_only=True)
    image = rest_serializers.SerializerMethodField()

    class Meta:
        model = product_models.Product
        fields = ('id', 'name', 'description', 'category', 'image',)

    def get_image(self, instance):
        if instance.image:
            return instance.image.url
        return None


class ProductPersonalitySerializer(rest_serializers.ModelSerializer):
    """
    Serializer for Product Personality
    """
    class Meta:
        model = product_models.ProductPersonality
        fields = ('id', 'quantity', 'unit',)


class ProductKeywordSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for product category
    """
    class Meta:
        model = product_models.ProductKeyword
        fields = ('id', 'name',)
