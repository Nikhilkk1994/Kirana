from __future__ import unicode_literals

from rest_framework import mixins as rest_mixins
from rest_framework import status as http_status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from customer import serilizers as customer_serilizers


class UserLogin(rest_mixins.CreateModelMixin, GenericViewSet):
    """
    ViewSet for login
    """
    serializer_class = customer_serilizers.UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        return Response(
            customer_serilizers.BaseUserSerializer(instance=user).data,
            status=http_status.HTTP_201_CREATED
        )


class UserSignUp(rest_mixins.CreateModelMixin, GenericViewSet):
    """
    View Set for user sign Up
    """
    serializer_class = customer_serilizers.UserSignSerializer
