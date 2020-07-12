from django.contrib import admin
from . models import Product,offer,bestseller,brand
# Register your models here.
admin.site.register(Product)
admin.site.register(offer)
admin.site.register(bestseller)
admin.site.register(brand)