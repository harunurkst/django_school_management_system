from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import EmployeeCreateForm

def create_employee(request):
    forms = EmployeeCreateForm()
    if request.method == 'POST':
        forms = EmployeeCreateForm(request.POST)
        print(forms)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user_obj = User.objects.create_user(username=username, password=password)
            new_user = forms.save(commit=False)  # store new object to a veriable
            new_user.user = user_obj  # add new user value
            new_user.save()  # now save to database
            print("ok")
            return redirect("home")

    context = {'forms': forms}
    return render(request, 'administration/create_employee.html', context)