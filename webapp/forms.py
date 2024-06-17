from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Rent


class CreateRentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = '__all__'
        error_messages = {
            'name': {
                'required': ''
            },
            'last_name': {
                'required': ''
            },
            'address': {
                'required': ''
            },
            'payment': {
                'required': ''
            },
            'vehicle': {
                'required': ''
            }
        }
