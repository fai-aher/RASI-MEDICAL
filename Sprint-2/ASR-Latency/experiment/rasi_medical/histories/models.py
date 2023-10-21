from django.db import models

# Create your models here.

class History(models.Model):
    patient_id = models.IntegerField()
    state = models.CharField(max_length=255)
    observations = models.CharField(max_length=255)
    
    # Modificar para que se guarde la historia del paciente, para que no se remplaze.
    # Añadir más atributos para que la historia clínica sea más completa. Por ejemplo, exámenes asignados para hacerse.

    def __str__(self):
        return self.state