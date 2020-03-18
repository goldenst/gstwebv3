from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from .models import SatsScores, DriverSats
from .forms import SatForm


class HomeView(View):
  def get(self, request, *args, **kwargs):
    qs = DriverSats.objects.all()
    sats = SatsScores.objects.all()
    context = {
      'driver_sats': qs,
      'sats': sats
    }
    return render(request, 'sats/view.html', context)

# get data ----------------------------------
def get_data(request, *args, **kwargs):
  qs = DriverSats.objects.all()
  context = {
    'driver_sats': qs
  }
  return render(request, 'sats/view.html', context )



def updateScores(request):
  return render(request, 'sats/update.html', {})

# rest view ==
class ChartData(APIView):
  
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
      # name = DriverSats.objects.all()
      labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
      default_items = [123,65,456,433,343,344]
      data= {
          'labels': labels,
          'defaultData': default_items
        
      }
      return Response(data)

#  results data
def resultsData(request):
  paid = DriverSats.objects.get(id=1)

  # for i in paid:
  #   paid.append({i.paidCalls})
    
  return JsonResponse(paid, safe=False)

def DriverViewSet(request, *args, **kwargs):
  return render(request, 'sats/view.html', {} )