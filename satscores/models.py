from django.db import models

# Create your models here.

class SatsScores(models.Model):
  month       = models.CharField(max_length=20)
  overall     = models.DecimalField(decimal_places=1, max_digits=3)
  driver      = models.DecimalField(decimal_places=1, max_digits=3)
  response    = models.DecimalField(decimal_places=1, max_digits=3)
  kmi         = models.DecimalField(decimal_places=1, max_digits=3)
  lostCalls   = models.IntegerField(default=0)
  aaacalls    = models.IntegerField(default=0)
  under60Min  = models.DecimalField(decimal_places=1, max_digits=3, default=0)

  def __str__(self):
    return self.month

class DriverSats(models.Model):
  name          = models.CharField(max_length=20,default=0)
  paidCalls     = models.IntegerField(default=0)
  rt60          = models.DecimalField(decimal_places=1, max_digits=4,default=0)
  tos           = models.DecimalField(decimal_places=1, max_digits=4,default=0)
  minIntow      = models.IntegerField(default=0)
  driversat     = models.DecimalField(decimal_places=1, max_digits=4,default=0)
  overallsat     = models.DecimalField(decimal_places=1, max_digits=4,default=0)
  is_active      = models.BooleanField(default=True)

  def __str__(self):
    return self.name