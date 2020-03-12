from django.db import models

# Create your models here.

class SatsScores(models.Model):
  month       = models.CharField(max_length=20)
  overall     = models.DecimalField(decimal_places=1, max_digits=3)
  driver      = models.DecimalField(decimal_places=1, max_digits=3)
  response    = models.DecimalField(decimal_places=1, max_digits=3)
  kmi         = models.DecimalField(decimal_places=1, max_digits=3)

  def __str__(self):
    return self.month