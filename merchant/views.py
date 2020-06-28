from rest_framework.decorators import action
from rest_framework import mixins as rest_mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from merchant import models as merchant_models
from merchant import serializer as merchant_serializer
from address.mixins import ActionSpecificSerializerMixin


class MerchantView(
    rest_mixins.ListModelMixin, rest_mixins.RetrieveModelMixin, ActionSpecificSerializerMixin, GenericViewSet
):
    """
    View to get the list of the Merchant.
    """
    serializer_classes = {
        'list': merchant_serializer.MerchantSerializer,
        'retrieve': merchant_serializer.MerchantSerializer,
        'products': merchant_serializer.MerchantMenuSerializer
    }

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

    @action(methods=['get'], detail=True,)
    def products(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
