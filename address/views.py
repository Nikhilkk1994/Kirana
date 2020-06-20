from __future__ import unicode_literals

from rest_framework import mixins as rest_mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status as http_status
from rest_framework import permissions as rest_permissions

from address import models as address_models
from address import serializer as address_serializer
from address import mixins as address_mixins


class UserAddressView(
    rest_mixins.ListModelMixin, rest_mixins.CreateModelMixin, address_mixins.ActionSpecificSerializerMixin, GenericViewSet
):
    """
    View Set for get the list of address of the Users
    """
    permission_classes = (rest_permissions.IsAuthenticated,)
    serializer_classes = {
        'list': address_serializer.UserAddressSerializer,
        'create': address_serializer.UserAddressCreateSerializer
    }

    def get_queryset(self):
        return address_models.Address.objects.filter(user__id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer = address_serializer.UserAddressSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=http_status.HTTP_201_CREATED)
