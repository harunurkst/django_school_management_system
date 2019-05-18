from django import forms 
from .models import StudentClassInfo, StudentShiftInfo


class SearchStudentForm(forms.Form):
    student_class = forms.ModelChoiceField(queryset=StudentClassInfo.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    section = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    roll = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    session = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))


class StudentRegistrationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    roll = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = forms.ChoiceField(choices=gender_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    fathers_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    std_class = forms.ModelChoiceField(queryset=StudentClassInfo.objects.all())
    std_shift = forms.ModelChoiceField(queryset=StudentShiftInfo.objects.all())
    session = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    section = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))



