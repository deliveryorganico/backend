from delivery_organico.models import *
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields=('id','city',)

class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Locality
        fields=('id','locality',)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('id','username','is_company', 'password')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields=('id','alias','address','floor','phone','st_number','zip_code','city','locality')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=('id','name','address')

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields=('id','reputation','n_phone','name','address','company')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('id','title','description','price','branch','photo')

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favorite
<<<<<<< HEAD
<<<<<<< HEAD
        fields=('profile','branch')
=======
        fields=('id','profile','branch')


>>>>>>> foto de producto agregada
=======
        fields=('id','profile','branch')


>>>>>>> 1910b75fdae62ae130a2a482624d4f606ce11489
