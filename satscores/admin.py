from django.contrib import admin

# Register your models here.
from .models import SatsScores
from .models import DriverSats


class SatScoresAdmin(admin.ModelAdmin):
  list_display = ('id','month','overall','response', 'driver', 'kmi', 'lostCalls', 'aaacalls', 'under60Min' ) 
  list_editable = ('month','overall','response', 'driver', 'kmi', 'lostCalls', 'aaacalls', 'under60Min')

class DriverSatsAdmin(admin.ModelAdmin):
  list_display = ('name','paidCalls','rt60', 'tos', 'minIntow','driversat', 'is_active' ) 
  list_editable = ('paidCalls','rt60', 'tos', 'minIntow','driversat', 'is_active')


admin.site.register(SatsScores, SatScoresAdmin)
admin.site.register(DriverSats, DriverSatsAdmin)