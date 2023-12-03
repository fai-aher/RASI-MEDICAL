from django import forms
from .models import History, Prescription, LabResult

class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = ['patient_id', 'state', 'observations', 'date_of_birth', 'blood_type', 'allergies', 'medications', 'past_diseases', 'surgeries', 'family_history']

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['medication', 'dosage']

class LabResultForm(forms.ModelForm):
    class Meta:
        model = LabResult
        fields = ['test_name', 'result']