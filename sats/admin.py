from django.contrib import admin

# Register your models here.
from .models import SatsScores
from .models import DriverSats


class SatScoresAdmin(admin.ModelAdmin):
  list_display = ('id','month','overall','response', 'driver', 'kmi' ) 
  list_editable = ('month','overall','response', 'driver', 'kmi')

class DriverSatsAdmin(admin.ModelAdmin):
  list_display = ('name','paidCalls','rt60', 'tos', 'missingOl', 'isActive' ) 
  list_editable = ('paidCalls','rt60', 'tos', 'missingOl', 'isActive')

admin.site.register(SatsScores, SatScoresAdmin)
admin.site.register(DriverSats, DriverSatsAdmin)