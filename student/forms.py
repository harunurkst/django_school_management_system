from django import forms 


class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}
        ))
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ))
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = forms.ChoiceField(choices=gender_choice, widget=forms.Select( 
        attrs={'class': 'form-control'}
        ))


