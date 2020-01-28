from django.db.models import Q
from django.db import models
from datetime import datetime
import random
import os


from sellers.models import Seller

# from django.db.models.signals import pre_save, post_save
from django.urls import reverse
# from goldenstateweb.utils import unique_slug_generator

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
class LienSaleManager(models.Manager):
  def featured(self):
    return self.get_queryset().filter(featured=True)

  def get_by_id(self,id):
    qs = self.get_queryset().filter(id=id)
    if qs.count() == 1:
      return qs.first()
    return None

  def search(self, query):
    lookups = Q(year__icontains=query) |Q(make__icontains=query ) | Q(model__icontains=query )
    return self.get_queryset().filter(lookups).distinct()


# ---------------- lien sale model --------------------------------
class LienSale(models.Model):
  seller        = models.ForeignKey(Seller, default=True, null=True, blank=True, on_delete=models.DO_NOTHING)
  yard          = models.CharField(max_length=20, default="Auburn")
  lot_num       = models.IntegerField(blank=True)
  year          = models.CharField(max_length=4, blank=True)
  make          = models.CharField(max_length=20, blank=True)
  model         = models.CharField(max_length=20, blank=True)
  vin           = models.CharField(max_length=17, blank=True)
  engine        = models.CharField(max_length=20, blank=True)
  fuel          = models.CharField(max_length=20, default="Gas")
  reg_date      = models.DateField(blank=True)
  catagory      = models.CharField(max_length=20, default="Cars")
  price         = models.IntegerField(default=0.00)
  odom          = models.IntegerField(blank=True)
  keys          = models.BooleanField(default=True)
  comment       = models.TextField(blank=True)
  avalible_date = models.DateField(blank=True)
  is_published  = models.BooleanField(default=True)
  featured      = models.BooleanField(default=False)
  photo_main    = models.ImageField(upload_to='liensales/')
  photo_1       = models.ImageField(upload_to='liensales/', blank=True)
  photo_2       = models.ImageField(upload_to='liensales/', blank=True)
  photo_3       = models.ImageField(upload_to='liensales/', blank=True)
  photo_4       = models.ImageField(upload_to='liensales/', blank=True)
  photo_5       = models.ImageField(upload_to='liensales/', blank=True)
  photo_6       = models.ImageField(upload_to='liensales/', blank=True)

  objects = LienSaleManager()

  def get_absolute_url(self):
    # return "/lien/{pk}/".format(pk=self.pk)
    return reverse("liens:detail", kwargs={'pk': self.pk})

  def __str__(self):
    return self.make
