from django import forms 
from .models import Employee


class EmployeeCreateForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField()
    
    class Meta:
        model = Employee
        fields = ('username', 'password', 'name', 'mobile', 'designation')