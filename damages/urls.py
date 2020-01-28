from django.urls import path

from .views import (
    damage_list_view, 
    damage_detail_view, 
    damage_create_view,
    )

app_name = 'damages'

urlpatterns = [
    path('', damage_list_view, name='list'),
    path('new/', damage_create_view),
    path('<pk>/', damage_detail_view, name='detail'),
]
