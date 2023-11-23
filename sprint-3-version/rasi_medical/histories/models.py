from django.db import models

class History(models.Model):
    patient_id = models.IntegerField()
    state = models.CharField(max_length=255)
    observations = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    blood_type = models.CharField(max_length=3)
    allergies = models.CharField(max_length=255)
    medications = models.CharField(max_length=255)
    past_diseases = models.CharField(max_length=255)
    surgeries = models.CharField(max_length=255)
    family_history = models.CharField(max_length=255)

    def __str__(self):
        return self.state
    
class HistoryEdit(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    edited_at = models.DateTimeField(auto_now_add=True)
    # Copia de cada campo en History
    patient_id = models.IntegerField()
    state = models.CharField(max_length=255)
    observations = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    blood_type = models.CharField(max_length=3)
    allergies = models.CharField(max_length=255)
    medications = models.CharField(max_length=255)
    past_diseases = models.CharField(max_length=255)
    surgeries = models.CharField(max_length=255)
    family_history = models.CharField(max_length=255)

class Prescription(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    medication = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)

class LabResult(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    result = models.CharField(max_length=255)