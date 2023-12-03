from django.db import models

class History(models.Model):
    patient_id = models.IntegerField(null=True)
    state = models.CharField(max_length=255, null=True)
    observations = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    blood_type = models.CharField(max_length=3, null=True)
    allergies = models.CharField(max_length=255, null=True)
    medications = models.CharField(max_length=255, null=True)
    past_diseases = models.CharField(max_length=255, null=True)
    surgeries = models.CharField(max_length=255, null=True)
    family_history = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.state
    
class HistoryEdit(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    edited_at = models.DateTimeField(auto_now_add=True)
    # Copia de cada campo en History
    patient_id = models.IntegerField(null=True)
    state = models.CharField(max_length=255, null=True)
    observations = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    blood_type = models.CharField(max_length=3, null=True)
    allergies = models.CharField(max_length=255, null=True)
    medications = models.CharField(max_length=255, null=True)
    past_diseases = models.CharField(max_length=255, null=True)
    surgeries = models.CharField(max_length=255, null=True)
    family_history = models.CharField(max_length=255, null=True)

class Prescription(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    medication = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)

class LabResult(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    result = models.CharField(max_length=255)