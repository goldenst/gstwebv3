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
class GarageSaleManager(models.Manager):
  def featured(self):
    return self.get_queryset().filter(featured=True)

  def get_by_id(self,id):
    qs = self.get_queryset().filter(id=id)
    if qs.count() == 1:
      return qs.first()
    return None


# ---------------- lien sale model --------------------------------
class GarageSale(models.Model):
  seller        = models.ForeignKey(Seller, default=True, on_delete=models.DO_NOTHING)
  yard          = models.CharField(max_length=20, default="Auburn")
  item          = models.CharField(max_length=100, blank=True)
  price         = models.IntegerField(default=0.00)
  details       = models.TextField(blank=True)
  is_published  = models.BooleanField(default=True)
  featured      = models.BooleanField(default=False)
  photo_main    = models.ImageField(upload_to='garageSale/')
  photo_1       = models.ImageField(upload_to='garageSale/', blank=True)
  photo_2       = models.ImageField(upload_to='garageSale/', blank=True)
  photo_3       = models.ImageField(upload_to='garageSale/', blank=True)
  photo_4       = models.ImageField(upload_to='garageSale/', blank=True)
  photo_5       = models.ImageField(upload_to='garageSale/', blank=True)
  photo_6       = models.ImageField(upload_to='garageSale/', blank=True)

  objects = GarageSaleManager()

  def get_absolute_url(self):
    # return "/lien/{pk}/".format(pk=self.pk)
    return reverse("garage:detail", kwargs={'pk': self.pk})

  def __str__(self):
    return self.item
