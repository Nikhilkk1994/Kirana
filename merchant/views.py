from rest_framework import mixins as rest_mixins
from rest_framework.viewsets import GenericViewSet

from merchant import models as merchant_models
from merchant import serializer as merchant_serializer


class MerchantView(rest_mixins.ListModelMixin, GenericViewSet):
    """
    View to get the list of the Merchant.
    """
    serializer_class = merchant_serializer.MerchantSerializer

    def get_queryset(self):
        """
        Filter the QuerySet
        :return: QuerySey Object
        """
        queryset = merchant_models.Merchant.objects.all()
        category_id = self.request.query_params.get('category', None)
        if category_id is not None:
            queryset = queryset.filter(
                id__in=merchant_models.MerchantProducts.objects.filter(
                    product__category__id=category_id
                ).values_list('merchant', flat=True)
            )
        return queryset
