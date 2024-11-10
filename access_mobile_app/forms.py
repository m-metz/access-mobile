from django import forms
from .models import DoneeAccount

class DoneeEditForm(forms.ModelForm):
    class Meta:
        model = DoneeAccount
        fields = ['name', 'bio']