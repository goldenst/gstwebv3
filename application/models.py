from django.db import models
from django.urls import reverse

YES_NO_CHOICES = (
  ('Yes', 'Yes'),
  ('No', 'No')
)

POSITION_CHOICES = (
  ('driver', 'Driver'),
  ('service', 'Service'),
  ('dispatcher', 'Dispatcher')
)

HOURS_CHOICES = (
  ('full', 'Full Time'),
  ('part', 'Part Time'),
  ('temp', 'Temp Work')
)

class ApplicationManager(models.Manager):
  def featured(self):
    return self.get_queryset().filter(featured=True)

  def get_by_id(self,id):
    qs = self.get_queryset().filter(id=id)
    if qs.count() == 1:
      return qs.first()
    return None

class JobApplication(models.Model):
  firstName                         = models.CharField(max_length=100)
  lastname                          = models.CharField(max_length=100)
  middleName                        = models.CharField(max_length=100)
  phoneNumber                       = models.CharField(max_length=100, default='0')
  email                             = models.EmailField(max_length=100, unique=True)
  address                           = models.CharField(max_length=100)
  address2                          = models.CharField(max_length=100, blank=True, null=True)
  city                              = models.CharField(max_length=100)
  state                             = models.CharField(max_length=100)
  zip                               = models.CharField(max_length=100)
  position                          = models.CharField(max_length=100, choices=POSITION_CHOICES, default='driver')
  hours                             = models.CharField(max_length=100, choices=HOURS_CHOICES, default='full')
  avalibility                       = models.CharField(max_length=100)
  start                             = models.CharField(max_length=100)
  reliableTransportation            = models.BooleanField(default=False)
  over18                            = models.BooleanField(default=False)
  drivingPosition                   = models.BooleanField(default=False)
  leaglyAbleToWork                  = models.BooleanField(default=False)
  essentialfuncrtons                = models.BooleanField(default=False)
  currentltEmployed                 = models.CharField(max_length=10, choices=YES_NO_CHOICES, default='No')
  contactEmployer                   = models.CharField(max_length=10, choices=YES_NO_CHOICES, default='No', blank=True, null=True)
  highSchool                        = models.CharField(max_length=100, blank=True, null=True)
  highSchoolCity                    = models.CharField(max_length=100, blank=True, null=True)
  graduated                         = models.CharField(max_length=10, choices=YES_NO_CHOICES, default='No', blank=True, null=True)
  highYearsattend                   = models.CharField(max_length=100, blank=True, null=True)
  highSchoolDegree                  = models.CharField(max_length=10, choices=YES_NO_CHOICES, default='No', blank=True, null=True)
  collage                           = models.CharField(max_length=100, blank=True, null=True)
  collageCity                       = models.CharField(max_length=100, blank=True, null=True)
  collageGraduate                   = models.CharField(max_length=10, choices=YES_NO_CHOICES, default='No', blank=True, null=True)
  collageYearsAttend                = models.CharField(max_length=100, blank=True, null=True)
  collagedegree                     = models.CharField(max_length=10, choices=YES_NO_CHOICES, default='No', blank=True, null=True)
  tradeSchool                       = models.CharField(max_length=100, blank=True, null=True)
  tradeSchoolCity                   = models.CharField(max_length=100, blank=True, null=True)
  tradeSchoolGraduate               = models.CharField(max_length=10, choices=YES_NO_CHOICES, default='No', blank=True, null=True)
  tradeSchoolYearsAttend            = models.CharField(max_length=100, blank=True, null=True)
  tradeSchoolDegree                 = models.CharField(max_length=10, choices=YES_NO_CHOICES, default='No', blank=True, null=True)
  previousEmployer1                 = models.CharField(max_length=100, blank=True, null=True)
  typeofbuisness1                   = models.CharField(max_length=100, blank=True, null=True)
  prevEmplouerAddress1              = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerPhone1            = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerSupervisor1       = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerRateofpay1        = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerDuties1           = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerReason1           = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerStart1            = models.DateField(auto_now=False, blank=True, null=True)
  previousEmployerEnd1              = models.DateField(auto_now=False, blank=True, null=True)
  previousEmployerContact1          = models.CharField(max_length=10, choices=YES_NO_CHOICES, default='No', blank=True, null=True)
  previousEmployer2                 = models.CharField(max_length=100, blank=True, null=True)
  typeofbuisness2                   = models.CharField(max_length=100, blank=True, null=True)
  prevEmplouerAddress2              = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerPhone2            = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerPhone2            = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerSupervisor2       = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerRateofpay2        = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerDuties2           = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerReason2           = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerStart2            = models.DateField(auto_now=False, blank=True, null=True)
  previousEmployerEnd2              = models.DateField(auto_now=False, blank=True, null=True)
  previousEmployerContact2          = models.CharField(max_length=10, choices=YES_NO_CHOICES, default='No', blank=True, null=True)
  previousEmployer3                 = models.CharField(max_length=100, blank=True, null=True)
  typeofbuisness3                   = models.CharField(max_length=100, blank=True, null=True)
  prevEmplouerAddress3              = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerPhone3            = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerSupervisor3       = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerRateofpay3        = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerDuties3           = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerReason3           = models.CharField(max_length=100, blank=True, null=True)
  previousEmployerStart3            = models.DateField(auto_now=False, blank=True, null=True)
  previousEmployerEnd3              = models.DateField(auto_now=False, blank=True, null=True)
  previousEmployerContact3          = models.CharField(max_length=10, choices=YES_NO_CHOICES, default='No', blank=True, null=True)
  createted_at                      = models.DateTimeField(auto_now_add=True)

  objects = ApplicationManager()

  def get_absolute_url(self):
    # return "/lien/{pk}/".format(pk=self.pk)
    return reverse("application:update", kwargs={'pk': self.pk})
  
  def __str__(self):
    return self.email
