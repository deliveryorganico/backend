from delivery_organico.models import *
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields=('id', 'alias', 'address', 'floor', 'phone', 'st_number', 'zip_code', 'city', 'locality')

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields=('id', 'reputation', 'n_phone', 'name', 'address', 'company')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields=('id', 'city')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=('id', 'name', 'address')

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favorite
        fields=('id', 'profile', 'branch')

class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Locality
        fields=('id', 'locality')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('id', 'title', 'description', 'price', 'branch', 'photo', 'created_at', 'updated_at')

class ProfileSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model=Profile
        fields=('id', 'username', 'first_name', 'last_name',  'is_company', 'password', 'photo', 'city', 'locality', 'address', 'floor', 'phone', 'st_number', 'zip_code')


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': ProfileSerializer(user, context={'request': request}).data
    }
