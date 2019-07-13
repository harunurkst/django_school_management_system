from django.urls import path
from . import views

urlpatterns = [
    path('attendance/<std_cls>/<std_roll>', views.StudentAttendancec.as_view(), name="search-student"),
    path('result', views.ResultView.as_view()),
    path('studentinfo/', views.StudentInfoView.as_view())
]
