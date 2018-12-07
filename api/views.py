from django.shortcuts import redirect

from delivery_organico.models import *
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import *


# Create your views here.
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    @action(methods=['GET', 'DELETE'], detail=True)
    def delete(self, request, pk, format=None):
        object = City.objects.get(pk=pk)
        object.delete()
        return redirect("../../")


class LocalityViewSet(viewsets.ModelViewSet):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer

    @action(methods=['GET', 'DELETE'], detail=True)
    def delete(self, request, pk, format=None):
        object = Locality.objects.get(pk=pk)
        object.delete()
        return redirect("../../")


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(methods=['GET', 'DELETE'], detail=True)
    def delete(self, request, pk, format=None):
        object = Profile.objects.get(pk=pk)
        object.delete()
        return redirect("../../")


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    @action(methods=['GET', 'DELETE'], detail=True)
    def delete(self, request, pk, format=None):
        object = Address.objects.get(pk=pk)
        object.delete()
        return redirect("../../")


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(methods=['GET', 'DELETE'], detail=True)
    def delete(self, request, pk, format=None):
        object = Company.objects.get(pk=pk)
        object.delete()
        return redirect("../../")


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    @action(methods=['GET', 'DELETE'], detail=True)
    def delete(self, request, pk, format=None):
        object = Branch.objects.get(pk=pk)
        object.delete()
        return redirect("../../")


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^title',)

    @action(methods=['GET', 'DELETE'], detail=True)
    def delete(self, request, pk, format=None):
        object = Product.objects.get(pk=pk)
        object.delete()
        return redirect("../../")


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    @action(methods=['GET', 'DELETE'], detail=True)
    def delete(self, request, pk, format=None):
        object = Favorite.objects.get(pk=pk)
        object.delete()
        return redirect("../../")
