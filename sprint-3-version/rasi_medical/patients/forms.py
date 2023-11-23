from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'name',
            'age',
            'email',
            'address',
        ]
        labels = {
            'name': 'Name',
            'age': 'Age',
            'email': 'Email',
            'address': 'Address',
        }