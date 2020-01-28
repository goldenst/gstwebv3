from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import GarageSale

# ----------------- list view ------------------------

def garage_sales_list_view(request):
  queryset = GarageSale.objects.all()
  context = {
    'title': ' Garage Sales',
    'object_list': queryset
  }
  return render(request, "garage/list.html", context)


# ----------------  detail View ---------------------------

def garage_sales_detail_view(request, pk=None, *args, **kwargs):
  instance = GarageSale.objects.get_by_id(pk)
  if instance is None:
    raise Http404("Garage Sale item does not Exsist!")
  context = {
    'title': 'Garage Sale Details',
    'object': instance
  }
  return render(request, "garage/detail.html", context)


# ---------------- Detail Slug view =============

# class lien_sales_detail_slug_view(DetailView):
#   queryset = LienSale.objects.all()
#   template_name = "lien/detail.html"

#  -------------------- features list view ------------------

# class lien_sales_featured_view(ListView):
#   template_name = "lien/list.html"

#   def get_queryset(self, *args, **kwargs):
#     request = self.request
#     return LienSale.objects.featured()

# ------------------- fetured detail view -------------------

# class lien_sales_featured_detail_view(DetailView):
#   template_name = "lien/featured-detail.html"

#   def get_queryset(self, *args, **kwargs):
#     request = self.request
#     return LienSale.objects.featured()