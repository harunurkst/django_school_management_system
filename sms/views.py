from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm


@login_required
def home(request):
    return render(request, 'home.html')


def user_login(request):
    forms = UserLoginForm()
    if request.method == 'POST':
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                print("wrong user")
    context = {'forms': forms}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')
