from django.contrib import admin
from vendor.models import Vendor, Food, VendorAdmin

# Register your models here.
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Food)
