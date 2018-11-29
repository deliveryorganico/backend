from delivery_organico.models import *
from rest_framework import serializers

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields=('city',)

class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Locality
        fields=('locality',)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('username','is_company',)

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields=('alias','address','floor','phone','st_number','zip_code','city','locality')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=('name','address')

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields=('reputation','n_phone','name','address','company')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('title','description','price','branch')

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favorite
        fields=('profile','branch')
