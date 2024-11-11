from django import forms
from .models import Farmer

class FarmerSignUpForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['username', 'email', 'phone_number', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }