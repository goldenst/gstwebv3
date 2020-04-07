from django.urls import path
from django.conf.urls import url


from .api import DriverViewSet, SatScoreViewSet
from .views import  HomeView

app_name = 'satscores'



urlpatterns = [

    path('', HomeView.as_view(), name='home'),

]

