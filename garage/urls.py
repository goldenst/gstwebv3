from django.urls import path

from .views import (
    garage_sales_list_view, 
    garage_sales_detail_view, 
    # lien_sales_featured_detail_view, 
    # lien_sales_featured_view,
    # lien_sales_detail_slug_view
    )

app_name = 'garage'

urlpatterns = [
   
    path('', garage_sales_list_view, name='list'),
    # path('featured/', lien_sales_featured_view.as_view()),
    # path('featured/<pk>/', lien_sales_feature'd_detail_view.as_view()),
    path('<pk>/', garage_sales_detail_view, name='detail'),
]

