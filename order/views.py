from rest_framework import mixins as rest_mixins
from rest_framework import status as http_status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from order import serializer as order_serializer
from merchant import views as merchant_views


class CartCheckOut(GenericViewSet, rest_mixins.CreateModelMixin):
    """
    ViewSet for Cart Checkout
    """
    # permission_classes = (rest_permissions.IsAuthenticated,)
    serializer_class = order_serializer.CartCheckoutSerializer
    pagination_class = merchant_views.MerchantProductsPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=http_status.HTTP_201_CREATED)
