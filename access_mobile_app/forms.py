from django import forms
from .models import DoneeAccount, DonorAccount

class DoneeEditForm(forms.ModelForm):
    class Meta:
        model = DoneeAccount
        fields = ['name', 'bio']

class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = DonorAccount
        fields = ['name', 'bio']  # Allow editing name and bio