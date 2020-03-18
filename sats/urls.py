from django.urls import path
from django.conf.urls import url
from rest_framework import routers

from .api import DriverViewSet, SatScoreViewSet
from .views import HomeView, updateScores, get_data, ChartData, resultsData

app_name = 'sats'

# router = routers.DefaultRouter()
# router.register('api/driver', DriverViewSet, 'driverSats')
# router.register('api/scores', SatScoreViewSet, 'Sats')


# urlpatterns = router.urls

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('api/data/', get_data),
    path('api/driver/', DriverViewSet),
    path('api/scores/sats', SatScoreViewSet),
    path('results/', resultsData),
    path('api/chart/data/', ChartData.as_view()),
    path('update/', updateScores, name='update'),
]

