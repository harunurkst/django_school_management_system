from django.urls import path, include
from . import views

urlpatterns = [
    path('employee/create/', views.create_employee, name="create-employee"),

]