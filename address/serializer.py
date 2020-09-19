from rest_framework import serializers as rest_serializers
from rest_framework import exceptions as rest_exceptions

from address import models  as address_models
from customer import models as customer_models


class UserAddressDetailSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for User Address Detail
    """
    class Meta:
        model = address_models.AddressDetail
        fields = ('city', 'state', 'country', 'zip_code',)


class UserAddressSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for User Address
    """
    address_detail = UserAddressDetailSerializer(read_only=True)

    class Meta:
        model = address_models.Address
        fields = ('id', 'area_house_number', 'landmark', 'address_detail',)


class UserAddressCreateSerializer(rest_serializers.Serializer):
    """
    Serializer to create the new Address
    """
    area_house_number = rest_serializers.CharField(help_text='address details', max_length=50)
    landmark = rest_serializers.CharField(help_text='landmark', max_length=50, required=False)
    city = rest_serializers.CharField(help_text='city', max_length=50)
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
            zip_code=validated_data.get('zip_code').lower(), city=validated_data.get('city').lower()
        )
        address = address_models.Address.objects.get_or_create(
            area_house_number=validated_data.get('area_house_number').lower(),
            landmark=validated_data.get('landmark').lower(), address_detail=address_detail[0]
        )
        # create address to user
        customer_models.UserToAddress.objects.get_or_create(user=self.context.get('request').user, address=address[0])
        return address

    def update(self, instance, validated_data):
        """
        Update the address of the user
        :param instance: instance of the Address
        :param validated_data: validate data
        :return: instance of the Address
        """
        address_detail = address_models.AddressDetail.objects.get_or_create(
            state=validated_data.get('state').lower(), country=validated_data.get('country').lower(),
            zip_code=validated_data.get('zip_code').lower(), city=validated_data.get('city').lower()
        )
        address = address_models.Address.objects.get_or_create(
            area_house_number=validated_data.get('area_house_number').lower(),
            landmark=validated_data.get('landmark').lower(), address_detail=address_detail[0]
        )[0]
        # delete the prev entry
        customer_models.UserToAddress.objects.filter(
            user=self.context.get('request').user, address=instance
        ).first().delete()
        # add the address of the user
        customer_models.UserToAddress.objects.get_or_create(user=self.context.get('request').user, address=address)
        return address
