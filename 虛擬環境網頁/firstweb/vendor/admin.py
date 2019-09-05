from django.contrib import admin

# Register your models here.
from .models import Vendor, Food

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Food)