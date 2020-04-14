from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import job_application

app_name = 'application'

urlpatterns = [
    path('', job_application, name='apply'),
]