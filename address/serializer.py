from rest_framework import serializers as rest_serializers

from address import models  as address_models


class UserAddressDetailSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for User Address Detail
    """
    class Meta:
        model = address_models.AddressDetail
        fields = ('state', 'country', 'zip_code',)


class UserAddressSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for User Address
    """
    address_detail = UserAddressDetailSerializer(read_only=True)

    class Meta:
        model = address_models.Address
        fields = ('area_house_number', 'landmark', 'address_detail',)
