from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_student, name="create-student"),
    path('register/', views.register_student, name="register-student"),
    path('edit/<int:pk>', views.edit_student, name="edit-student"),
    path('list/', views.student_list, name="student-list"),
    path('search/', views.search_student, name="search-student"),
    path('att-count/', views.attendance_count, name="att-count"),
]
