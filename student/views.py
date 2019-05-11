from django.shortcuts import render
from .models import StudentInfo
from .forms import StudentForm


def create_student(request):
    if request.method == 'POST':
        forms = StudentForm(request.POST)
        if forms.is_valid():
            std_name = forms.cleaned_data["name"]
            std_age = forms.cleaned_data["age"]
            std_gender = forms.cleaned_data["gender"]

            try:
                StudentInfo.objects.create(
                    name=std_name,
                    age=std_age,
                    gender=std_gender
                )
            except Exception as err:
                print("error: ", err)
        else:
            print("error:",forms.error)
        
    forms = StudentForm()
    context = {'forms': forms}
    return render(request, 'student/create_std.html', context)



