from django.contrib import admin

# Register your models here.
from .models import GarageSale

class GarageSaleAdmin(admin.ModelAdmin):
  list_display = ('id','yard', 'is_published','item', 'price',) 
  list_display_links = ('id', 'item')
  list_filter = ('seller',)
  list_editable = ('is_published',)
  list_per_page = 25

admin.site.register(GarageSale, GarageSaleAdmin)