from django.urls import path
from . import views

urlpatterns = [
    path('attendance/<std_cls>/<std_roll>', views.std_attendance, name="search-student"),

]
