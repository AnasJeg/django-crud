from django import forms
from cours.models import Patient


class PatientF(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['nom', 'date','type']
        widgets = {'nom': forms.TextInput(attrs={'class': 'form-control'}),
                   'date' : forms.DateTimeInput(attrs={'class': 'form-control'}),
                   'type': forms.TextInput(attrs={'class': 'form-control'})
                   }
