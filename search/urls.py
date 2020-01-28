from django.urls import path

from .views import (
   SearchLienView,
    )

app_name = 'liens'

urlpatterns = [
    path('', SearchLienView.as_view() , name='query'),
]