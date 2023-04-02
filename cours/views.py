from django.shortcuts import render
from .models import Patient

def patient_list(request):
    patient = Patient.objects.all()
    return render(request, 'index.html', {'patient': patient})