from django.db import models


class Patient(models.Model):
    nom = models.CharField(max_length=50)
    date = models.DateField()
    type = models.BooleanField()
    
    class Meta:
        db_table = "patientdb"
