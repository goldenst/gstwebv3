from django.urls import path

from .views import (
    employee_create_view,
    employee_detail_view,
    employee_list_view
    )

app_name = 'employees'

urlpatterns = [
    path('', employee_list_view, name='list'),
    path('<pk>/', employee_detail_view, name='detail'), 
    path('new/', employee_create_view), 
]
