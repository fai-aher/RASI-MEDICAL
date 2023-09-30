from django.db import models

# Create your models here.

class History(models.Model):
    patient_id = models.IntegerField()
    state = models.CharField(max_length=255)
    observations = models.CharField(max_length=255)
    # Add any other fields you need for your patient model

    def __str__(self):
        return self.state