from django.db import models
from datetime import datetime
import random
import os

# from django.db.models.signals import pre_save, post_save
from django.urls import reverse
# from goldenstateweb.utils import unique_slug_generator

# from drivers.models import Driver
from employees.models import Employee
# Create your models here.

# -------------------------  create new file for images --------------------
def get_filename_ext(filepath):
  base_name = os.path.basename(filepath)
  name, ext = os.path.splitext(base_name)
  return name, ext

def upload_image_path(instance, filename):
  print(instance)
  print(filename)
  new_filename = random.randint(1, 9999999999)
  name, ext = get_filename_ext(filename)
  final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
  return "products/{new_filename}/{final_filename}".format(
          new_filename=new_filename, 
          final_filename=final_filename
          )

# -------------------- Lien sale model Manager ----------------------------
class DamagesManager(models.Manager):
  def featured(self):
    return self.get_queryset().filter(featured=True)

  def get_by_id(self,id):
    qs = self.get_queryset().filter(id=id)
    if qs.count() == 1:
      return qs.first()
    return None

DAMAGE_STATUS_CHOICES = (
  ('reported', 'Reported'),
  ('investigating', 'Investigating'),
  ('insurance', 'Turned into Insurance'),
  ('waiting', 'Waiting for Cust '),
  ('inprocess', 'Repair in Process'),
  ('denied', 'Denied'),
  ('closed', 'Closed'),
)

class Damage(models.Model):
  employee            = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
  date_of_incident    = models.DateField(blank=True)
  club                = models.CharField(blank=True, max_length=120)
  call_num            = models.IntegerField(blank=True)
  customer_email      = models.CharField(blank=True, max_length=120)
  cust_name           = models.CharField(blank=True, max_length=120)
  cust_phone          = models.CharField(blank=True, max_length=120)
  vehicle             = models.CharField(max_length=120)
  damages             = models.CharField(blank=True, max_length=120)
  damage_notes        = models.TextField(blank=True)
  status              = models.CharField(max_length=120, default='Reported', choices=DAMAGE_STATUS_CHOICES)
  cost_to_gst         = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
  repaired_at         = models.CharField(blank=True, max_length=120)
  closed              = models.BooleanField(default=False)
  closed_date         = models.DateField(blank=True, null=True)
  damages_est         = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
  estimate            = models.FileField(upload_to='damages/', blank=True)
  driver_statement    = models.FileField(upload_to='damages/', blank=True)
  damage_main         = models.ImageField(upload_to='damages/', blank=True)
  damage_2            = models.ImageField(upload_to='damages/', blank=True)
  damage_3            = models.ImageField(upload_to='damages/', blank=True)
  damage_4            = models.ImageField(upload_to='damages/', blank=True)
  damage_5            = models.ImageField(upload_to='damages/', blank=True)
  damage_6            = models.ImageField(upload_to='damages/', blank=True)
  damage_7            = models.ImageField(upload_to='damages/', blank=True)
  damage_8            = models.ImageField(upload_to='damages/', blank=True)
  damage_9            = models.ImageField(upload_to='damages/', blank=True)

  objects = DamagesManager()

  def get_absolute_url(self):
    # return "/lien/{pk}/".format(pk=self.pk)
    return reverse("damages:detail", kwargs={'pk': self.pk})

  def __str__(self):
    return self.cust_name