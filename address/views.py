from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework import mixins as rest_mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status as http_status
from rest_framework import permissions as rest_permissions


from address import models as address_models
from address import serializer as address_serializer
from address import mixins as address_mixins
from customer import models as customer_models


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
        'create': address_serializer.UserAddressCreateSerializer,
        'update': address_serializer.UserAddressCreateSerializer
    }
    pagination_class = None

    def get_queryset(self):
        query_filter = Q(user__id=self.request.user.id)
        param_id = self.kwargs.get('pk', None)
        if param_id:
            query_filter &= Q(id=param_id)
        return address_models.Address.objects.filter(query_filter)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer = address_serializer.UserAddressSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=http_status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer = address_serializer.UserAddressSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=http_status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        # check user have this address field
        address = get_object_or_404(self.get_queryset(), id=self.kwargs.get(self.lookup_field))
        customer_models.UserToAddress.objects.filter(address=address, user=self.request.user.id).first().delete()
        return Response(status=http_status.HTTP_204_NO_CONTENT)
