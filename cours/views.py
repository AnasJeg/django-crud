from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientF


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'index.html', {'patients': patients})


def add(request):
    if request.method == "POST":
        form = PatientF(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:  
                pass
    else:
        form = PatientF()
    return render(request,'ajouter.html',{'form':form}) 

def update(request, id):  
    patient = Patient.objects.get(id=id)  
    form = PatientF(request.POST, instance = patient)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'update.html', {'patient': patient})  

def delete(request, id):  
    patient = Patient.objects.get(id=id)  
    patient.delete()  
    return redirect("/") 
