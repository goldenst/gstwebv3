from django.db import models

class Employee(models.Model):
  aaaDriverNumber       = models.CharField(max_length=8, null=True, blank=True)
  firstName             = models.CharField(max_length=50)
  lastName              = models.CharField(max_length=50)
  address               = models.CharField(max_length=50)
  city                  = models.CharField(max_length=50)
  state                 = models.CharField(max_length=2)
  zipCode               = models.IntegerField()
  email                 = models.EmailField(max_length=200, unique=True, null=True, blank=True)
  driversLicence        = models.CharField(max_length=10, null=True, blank=True)
  dlExpire              = models.DateField(auto_now=False)
  cellphone             = models.CharField(max_length=10)
  homePhone             = models.CharField(max_length=10, null=True, blank=True)
  hiredate              = models.DateField(auto_now=False)
  emergencyContact      = models.CharField(max_length=100, null=True, blank=True)
  emerContactPhone      = models.CharField(max_length=10, null=True, blank=True)
  emerContactRelation   = models.CharField(max_length=20, null=True, blank=True)
  isDriver              = models.BooleanField(default=False)
  isDispatcher          = models.BooleanField(default=False)
  isManager             = models.BooleanField(default=False)
  termDate              = models.DateField(auto_now=False)
  notes                 = models.TextField(blank=True, null=True)
  created_at            = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return self.firstName