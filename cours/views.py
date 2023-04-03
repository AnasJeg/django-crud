from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientF


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'index.html', {'patients': patients})


def ajouter(request):
    if request.method == "POST":
        form = PatientF(request.POST)
        if form.is_valid():
                form.save()
                return redirect('/')
    else:
        form = PatientF()
    return render(request,'ajouter.html', {'form': form})
