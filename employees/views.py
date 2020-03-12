from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Employee
from .forms import EmployeeForm


# ----------------- list view ------------------------

def employee_list_view(request):
  queryset = Employee.objects.all()
  context = {
    'title': ' Employees',
    'object_list': queryset
  }
  return render(request, "employees/list.html", context)


# ----------------  detail View ---------------------------

def employee_detail_view(request, pk=None, *args, **kwargs):
  instance = Employee.objects.get_by_id(pk)
  if instance is None:
    raise Http404("Employee does not Exsist!")
  context = {
    'title': 'Employee Details',
    'object': instance
  }
  return render(request, "employees/detail.html", context)

  # --------------- Create view ---------------------------
def employee_create_view(request):
  form = EmployeeForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = EmployeeForm()

  context = {
    'form' : form,
    }
  return render(request, 'employees/new.html', context)