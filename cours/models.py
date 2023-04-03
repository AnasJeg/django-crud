from django.db import models


class Patient(models.Model):
    nom = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    type = models.BooleanField()
    
    class Meta:
        db_table = "patientdb"
