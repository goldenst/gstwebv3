from django.contrib import admin

# Register your models here.
from .models import Seller

class SellerAdmin(admin.ModelAdmin):
  list_display = ('id','name')


admin.site.register(Seller, SellerAdmin)