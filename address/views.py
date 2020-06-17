from __future__ import unicode_literals

from rest_framework import mixins as rest_mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions as rest_permissions

from address import models as address_models
from address import serializer as address_serializer


class UserAddressView(rest_mixins.ListModelMixin, GenericViewSet):
    """
    View Set for get the list of address of the Users
    """
    permission_classes = (rest_permissions.IsAuthenticated,)
    serializer_class = address_serializer.UserAddressSerializer

    def get_queryset(self):
        return address_models.Address.objects.filter(user__id=self.request.user.id)
