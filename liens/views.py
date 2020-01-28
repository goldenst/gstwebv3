from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import LienSale
from sellers.models import Seller

# ----------------- list view ------------------------

def lien_sales_list_view(request):
  queryset = LienSale.objects.all()
  context = {
    'title': ' Lien Sales',
    'object_list': queryset
  }
  return render(request, "lien/list.html", context)

# class lien_sales_list_view(ListView):
#   template_name = "lien/list.html"

#   def get_queryset(self, *args, **kwargs):
#     request = self.request
#     return LienSale.objects.all()


# ----------------  detail View ---------------------------

def lien_sales_detail_view(request, pk=None, *args, **kwargs):
  instance = LienSale.objects.get_by_id(pk)
  if instance is None:
    raise Http404("Lien Sale does not Exsist!")
  context = {
    'title': 'Lien Sale Details',
    'object': instance
  }
  return render(request, "lien/detail.html", context)


# ------------------- Search View -----------------------------



# ---------------- Detail Slug view =============

# class lien_sales_detail_slug_view(DetailView):
#   queryset = LienSale.objects.all()
#   template_name = "lien/detail.html"

# #  -------------------- features list view ------------------

# class lien_sales_featured_view(ListView):
#   template_name = "lien/list.html"

#   def get_queryset(self, *args, **kwargs):
#     request = self.request
#     return LienSale.objects.featured()

# # ------------------- fetured detail view -------------------

# class lien_sales_featured_detail_view(DetailView):
#   template_name = "lien/featured-detail.html"

#   def get_queryset(self, *args, **kwargs):
#     request = self.request
#     return LienSale.objects.featured()