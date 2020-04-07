# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import authentication, permissions

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View, ListView

# Create your views here.
from .models import DriverSats, SatsScores 
from .forms import SatForm

# class SatListView(ListView):
#   context_object_name = 'drivers'
#   model = models.DriverSats
  

class HomeView(View):
  def get(self, request, *args, **kwargs):
    qs = DriverSats.objects.all()
    sat = SatsScores.objects.all()
    context = {
      'driver': qs,
      'sats': sat
    }
    return render(request, 'sats/view.html', context)



