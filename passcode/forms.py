from models import *
from django.forms import ModelForm

class PasscodeRequestForm(ModelForm):
    class Meta:
        model = PasscodeRequest
        fields = ('full_name', 'callsign', 'locator', 'email', 'comment')
