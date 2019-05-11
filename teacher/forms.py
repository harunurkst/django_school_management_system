from django import forms 
from .models import TeacherInfo


class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherInfo
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
        }