from django.urls import path

from .views import (
   SearchLienView,
    )

app_name = 'search'

urlpatterns = [
    path('', SearchLienView.as_view() , name='query'),
]