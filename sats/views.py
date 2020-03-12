
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.
from .models import SatsScores
from .forms import SatForm


def satScores(request):
  queryset = SatsScores.objects.all()
  context = { 
    'title': 'Sat Scores',
    'object_list': queryset
  }
  return render(request, 'sats/view.html', context)

# get data ----------------------------------
def get_data(request, *args, **kwaargs):
  data = {
    'overall': 88,
    'driver': 90.9,
    'response': 56.6,
    'kmi': 78.8
  }
  return JsonResponse(data)



def updateScores(request):
  return render(request, 'sats/update.html', {})

class ChartData(APIView):
  
  authentication_classes = []
  permission_classes = []

  def get(self, request, format=None):
    overall = qs.satScores.overall()
      data = {
        'overall': overall,
        'driver': 90.9,
        'response': 56.6,
        'kmi': 78.8
      }
      return Response(data)



