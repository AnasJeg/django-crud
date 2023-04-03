from django import forms
from cours.models import Patient


class PatientF(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['nom', 'type']
        widgets = {'nom': forms.TextInput(attrs={'class': 'form-control'}),
                   'type': forms.TextInput(attrs={'class': 'form-control'}),
                   }
