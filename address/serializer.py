from rest_framework import serializers as rest_serializers

from address import models  as address_models
from customer import models as customer_models


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


class UserAddressCreateSerializer(rest_serializers.Serializer):
    """
    Serializer to create the new Address
    """
    area_house_number = rest_serializers.CharField(help_text='address details', max_length=50)
    landmark = rest_serializers.CharField(help_text='landmark', max_length=50, required=False)
    state = rest_serializers.CharField(help_text='state', max_length=50)
    country = rest_serializers.CharField(help_text='country', max_length=50)
    zip_code = rest_serializers.CharField(help_text='zip code', max_length=50)

    def create(self, validated_data):
        """
        To create the new Adrress for the user
        :param validated_data: Validate data
        :return: instance of the address
        """
        address_detail = address_models.AddressDetail.objects.get_or_create(
            state=validated_data.get('state').lower(), country=validated_data.get('country').lower(),
            zip_code=validated_data.get('zip_code').lower()
        )
        print(address_detail)
        address = address_models.Address.objects.get_or_create(
            area_house_number=validated_data.get('area_house_number').lower(),
            landmark=validated_data.get('landmark').lower(), address_detail=address_detail[0]
        )
        # create address to user
        address_to_user = customer_models.UserToAddress.objects.get_or_create(
            user=self.context.get('request').user, address=address[0]
        )
        return address_to_user
