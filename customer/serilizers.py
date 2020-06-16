from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from rest_framework.authtoken.models import Token
from rest_framework import (
    serializers as rest_serializers,
    exceptions as rest_exceptions
)

from customer import models as customer_models


class BaseUserSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for user(customer, ect)
    """
    access_token = rest_serializers.SerializerMethodField()

    class Meta:
        model = customer_models.User
        fields = ('mobile', 'first_name', 'last_name', 'access_token',)

    def get_access_token(self, instance):
        return Token.objects.get(user=instance).key


class UserLoginSerializer(rest_serializers.Serializer):
    """
    Serializer for User Login In
    """
    mobile = rest_serializers.IntegerField(label=_('Mobile'))
    password = rest_serializers.CharField(
        label=_('Password'), write_only=True, style={'input_type': 'password'}
    )

    def validate(self, attrs):
        user = customer_models.User.objects.filter(mobile=attrs.get('mobile')).first()
        if not user or not user.check_password(attrs.get('password')):
            raise rest_exceptions.ValidationError(_('Mobile/Password is incorrect.'))
        attrs['user'] = user
        return attrs


class UserSignSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for User Sign Up
    """
    access_token = rest_serializers.SerializerMethodField()

    class Meta:
        model = customer_models.User
        fields = ('mobile', 'first_name', 'last_name', 'password', 'access_token',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_access_token(self, instance):
        return Token.objects.get(user=instance).key

    def create(self, validated_data):
        """
        Create the User Object
        """
        instance = customer_models.User.objects.create(**validated_data)
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
