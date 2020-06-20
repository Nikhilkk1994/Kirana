from rest_framework import serializers as rest_serializers

from product import models as product_models


class CategorySerializer(rest_serializers.ModelSerializer):
    """
    Serializer for category
    """
    class Meta:
        model = product_models.Category
        fields = ('id', 'name', 'url',)
