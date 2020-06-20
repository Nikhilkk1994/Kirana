from __future__ import unicode_literals

from django.shortcuts import get_object_or_404

from rest_framework import mixins as rest_mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status as http_status
from rest_framework import permissions as rest_permissions


from address import models as address_models
from address import serializer as address_serializer
from address import mixins as address_mixins
from customer import models as customer_address


class UserAddressView(
    rest_mixins.ListModelMixin, rest_mixins.CreateModelMixin, rest_mixins.DestroyModelMixin,
    address_mixins.ActionSpecificSerializerMixin, GenericViewSet
):
    """
    View Set for get the list of address of the Users
    """
    permission_classes = (rest_permissions.IsAuthenticated,)
    serializer_classes = {
        'list': address_serializer.UserAddressSerializer,
        'create': address_serializer.UserAddressCreateSerializer
    }
    lookup_field = 'address_id'

    def get_queryset(self):
        return address_models.Address.objects.filter(user__id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer = address_serializer.UserAddressSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=http_status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        # check user have this address field
        address = get_object_or_404(self.get_queryset(), id=self.kwargs.get(self.lookup_field))
        address.delete()
        return Response(status=http_status.HTTP_204_NO_CONTENT)
