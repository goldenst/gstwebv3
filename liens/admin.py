from django.contrib import admin

# Register your models here.
from .models import LienSale
from sellers.models import Seller

class LienSaleAdmin(admin.ModelAdmin):
  list_display = ('id','yard', 'is_published', 'featured', 'year','make','model', 'price',) 
  list_display_links = ('id', 'make')
  list_filter = ('seller',)
  list_editable = ('is_published',)
  search_fields = ('year', 'make', 'model',)
  list_per_page = 25

admin.site.register(LienSale, LienSaleAdmin)