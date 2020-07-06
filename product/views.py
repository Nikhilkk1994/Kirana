from rest_framework import mixins as rest_mixins
from rest_framework.viewsets import GenericViewSet

from product import models as product_models
from product import serializer as product_serializer
from merchant.views import MerchantProductsPagination


class CategoryView(rest_mixins.ListModelMixin, GenericViewSet):
    """
    View Set for get the list of Category
    """
    serializer_class = product_serializer.CategorySerializer
    queryset = product_models.Category.objects.all()
    pagination_class = MerchantProductsPagination

