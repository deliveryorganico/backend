from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(City)
admin.site.register(Locality)
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Product)
admin.site.register(Favorite)