from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import job_application_create, application_list, job_application_edit

app_name = 'application'

urlpatterns = [
    path('', job_application_create, name='apply'),
    path('application-list/', application_list, name='list'),
    path('application/<pk>/', job_application_edit, name='update'),
]