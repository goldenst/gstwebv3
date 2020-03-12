from django import forms

from .models import SatsScores

# User = get_user_model()

class SatForm(forms.ModelForm):
  class Meta:
    model = SatsScores
    fields = '__all__'