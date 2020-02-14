from django.contrib import admin

# Register your models here.
from .models import Damage



class DamageAdmin(admin.ModelAdmin):
  list_display = ('id','cust_name','cost_to_gst','date_of_incident', 'status', 'employee' ) 
  list_display_links = ('id', 'cust_name')
  list_editable = ('status',)
  search_fields = ('employee', 'cust_name')
  list_per_page = 25


admin.site.register(Damage, DamageAdmin)