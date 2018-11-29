from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from .views import *
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router=DefaultRouter()
router.register(r'city', CityViewSet,base_name="city")
router.register(r'profile',ProfileViewSet,base_name="profile")
router.register(r'locality',LocalityViewSet,base_name="locality")
router.register(r'address', AddressViewSet,base_name='address')
router.register(r'company', CompanyViewSet, base_name='company')
router.register(r'branch', BranchViewSet, base_name='branch')
router.register(r'product', ProductViewSet, base_name='product')
router.register(r'favorite', FavoriteViewSet, base_name='favorite')
urlpatterns=router.urls


urlpatterns = [
    path('rest/', include(router.urls)),
    path('auth/obtain_token/', obtain_jwt_token),
    path('auth/refresh_token/', refresh_jwt_token),
]