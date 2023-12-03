from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=255)
    # Add any other fields you need for your patient model

    def __str__(self):
        return self.name