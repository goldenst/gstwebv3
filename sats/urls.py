from django.urls import path
from django.conf.urls import url


from .views import satScores, updateScores, get_data, ChartData

app_name = 'sats'

urlpatterns = [
   
    path('', satScores),
    path('api/data', get_data, name='api-data'),
    path('api/chart/data', ChartData.as_view()),
    path('update/', updateScores, name='update'),
  
]

