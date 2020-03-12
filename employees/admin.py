from django.contrib import admin

# Register your models here.
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
  list_display = ('id','firstName','lastName','cellphone', 'isDriver', 'isManager' ) 
  list_display_links = ('id', 'firstName')
  list_per_page = 25


admin.site.register(Employee, EmployeeAdmin)