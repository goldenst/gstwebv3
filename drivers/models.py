from django.db import models

# Create your models here.
class Driver(models.Model):
  name      = models.CharField(max_length=200)
  phone     = models.CharField(max_length=20)
  email     = models.CharField(max_length=50)
  cell      = models.CharField(max_length=20, blank=True, null=True)
  cdl       = models.CharField(max_length=20, blank=True, null=True)
  cdlexp    = models.DateField(blank=True, null=True)
  tsac      = models.DateField(blank=True, null=True)
  wm23      = models.DateField(blank=True, null=True)
  wm45      = models.DateField(blank=True, null=True)
  wm67      = models.DateField(blank=True, null=True)
  wm89      = models.DateField(blank=True, null=True)
  hireDate  = models.DateField(blank=True, null=True)
  
  def __str__(self):
    return self.name