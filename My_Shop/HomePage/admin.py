from django.contrib import admin
from . models import Product,offer,bestseller,brand,Contact
# Register your models here.
admin.site.register(Product)
admin.site.register(offer)
admin.site.register(bestseller)
admin.site.register(brand)
admin.site.register(Contact)