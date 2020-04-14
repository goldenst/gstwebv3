from django.shortcuts import render




def job_application(request):
  # form = job_applicationForm(request.POST or None)
  context = {
    'title': "Now accepting Applicastions",
  }
  return render(request, 'job-app.html', context)
