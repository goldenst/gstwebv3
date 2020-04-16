from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect

from .forms import JobApplicationForm
from .models import JobApplication




def job_application_create(request):
  form = JobApplicationForm(request.POST or None)
  if form.is_valid():
    form.save()
  form = JobApplicationForm()  
  context = {
    'title': "Now accepting Applications",
    'form': form
  }
  return render(request, 'job-app.html', context)




def job_application_edit(request, pk=None):
  instance = get_object_or_404(JobApplication, pk=pk)
  form = JobApplicationForm(request.POST or None, instance=instance)
  context = {
      'title': "Employee Applications",
      'instance': instance,
      'form': form,
    }
  
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()

  return render(request, 'job-app.html', context)



def application_list(request):
  instance = JobApplication.objects.order_by('-id')
  context = {
    'jobs': instance,
  }
  return render(request, 'application/list.html', context)