
from django.shortcuts import render
from django.views.generic import ListView

from liens.models import LienSale

class SearchLienView(ListView):
  template_name = "search/view.html"

  def get_queryset(self, *args, **kwargs):
    request = self.request
    method_dict = request.GET
    # print(request.GET)
    query = method_dict.get('q', None)
    # print(query)
    if query is not None:
      return LienSale.objects.search(query)
    return LienSale.objects.featured()

