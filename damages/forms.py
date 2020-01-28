
from django import forms

from .models import Damage

class DamageForm(forms.ModelForm):
  class Meta:
    model = Damage
    fields = [
      'driver',
      'date_of_incident',
      'club',
      'call_num',
      'customer_email',
      'cust_name',
      'cust_phone',
      'vehicle',
      'damages',
      'damage_notes',
      'status',
      'cost_to_gst',
      'repaired_at',
      'closed',
      'closed_date',
      'damages_est',
      'estimate',
      'driver_statement',
      'damage_main',
      'damage_2',
      'damage_3',
      'damage_4',
      'damage_5',
      'damage_6',
      'damage_7',
      'damage_8',
      'damage_9',
    ]
    
