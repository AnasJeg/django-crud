from django.db import models


class Patient(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    type = models.TextField()

def __str__(self):
    return self.title
