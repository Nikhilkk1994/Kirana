from rest_framework.decorators import action
from rest_framework import mixins as rest_mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import pagination as rest_pagination
from rest_framework import exceptions as rest_exceptions

from django.core.paginator import InvalidPage

from merchant import models as merchant_models
from merchant import serializer as merchant_serializer
from address.mixins import ActionSpecificSerializerMixin
from address import models as address_models


class MerchantProductsPagination(rest_pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    invalid_page_message = 'Page out of range'


class MerchantView(
    rest_mixins.ListModelMixin, rest_mixins.RetrieveModelMixin, ActionSpecificSerializerMixin, GenericViewSet
):
    """
    View to get the list of the Merchant.
    """
    serializer_classes = {
        'list': merchant_serializer.MerchantSerializer,
        'retrieve': merchant_serializer.MerchantSerializer
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
        zip_code = self.request.query_params.get('zip_code', None)
        if zip_code:
            address = address_models.AddressDetail.objects.filter(zip_code=zip_code)
            if not address.exists():
                queryset = merchant_models.Merchant.objects.none()
            else:
                queryset = queryset.filter(serve_zip_code__in=[address.first().id])
        return queryset


class MerchantProductView(GenericViewSet):
    """
    View is for get the merchant products
    """
    serializer_class = merchant_serializer.MerchantProductSerializer
    pagination_class = MerchantProductsPagination

    def get_queryset(self):
        queryset = merchant_models.MerchantProducts.objects.filter(merchant=self.get_object())
        category_id = self.request.query_params.get('category', None)
        if category_id is not None:
            queryset = queryset.filter(product__category__id=category_id)
        return queryset

    def get_object(self):
        """
        Validate the merchant object(ID)
        :return: Merchant Object
        """
        # verify the merchant exists and applied the filter for query params
        if not merchant_models.Merchant.objects.filter(id=self.kwargs.get(self.lookup_field)).exists():
            raise rest_exceptions.NotFound('ID with {} Merchant Not Exists'.format(self.kwargs.get(self.lookup_field)))
        zip_code = self.request.query_params.get('zip_code', None)
        if zip_code:
            address = address_models.AddressDetail.objects.filter(zip_code=zip_code)
            if not address.exists():
                raise rest_exceptions.NotFound('Zip Code with value {} not exists'.format(zip_code))
            if (
                address.exists() and not
                merchant_models.Merchant.objects.filter(
                    id=self.kwargs.get(self.lookup_field), serve_zip_code__in=[address.first().id]
                ).exists()
            ):
                raise rest_exceptions.NotFound('Merchant with ID {} not serve in zip code {}'.format(
                    self.kwargs.get(self.lookup_field), zip_code)
                )
        return merchant_models.Merchant.objects.get(id=self.kwargs.get(self.lookup_field))

    @action(methods=['get'], detail=True,)
    def products(self, request, pk=None):
        page = self.paginate_queryset(self.get_queryset())
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
