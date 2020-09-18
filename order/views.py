from rest_framework import (
    mixins as rest_mixins,
    status as http_status,
    exceptions as rest_exceptions,
)
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from order import serializer as order_serializer
from merchant import views as merchant_views
from merchant import  models as merchant_models


class CartCheckOut(GenericViewSet, rest_mixins.CreateModelMixin):
    """
    ViewSet for Cart Checkout
    """
    # permission_classes = (rest_permissions.IsAuthenticated,)
    serializer_class = order_serializer.CartCheckoutSerializer
    pagination_class = merchant_views.MerchantProductsPagination

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
            'merchant_id': self.kwargs.get('pk')
        }

    @action(methods=('post',), detail=True)
    def checkout(self, request, *args, **kwargs):
        # verify merchant ID exists
        merchant = merchant_models.Merchant.objects.filter(id=kwargs.get('pk'))
        if not merchant.exists():
            raise rest_exceptions.ValidationError('Merchant with ID {} not exists'.format(kwargs.get('pk')))
        zip_code = self.request.query_params.get('zip_code', None)
        if zip_code and not merchant.first().serve_zip_code.filter(zip_code=zip_code).exists():
            raise rest_exceptions.ValidationError('Merchant with ID {} not serve in zip code {}'.format(
                kwargs.get('pk'), zip_code)
            )
        context = self.get_serializer_context()
        serializer = self.get_serializer(data=request.data, many=True, context=context)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=http_status.HTTP_201_CREATED)
