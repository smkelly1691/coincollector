from django.forms import ModelForm
from .models import Appraising

class AppraisingForm(ModelForm):
  class Meta:
    model = Appraising
    fields = ['date', 'type']
