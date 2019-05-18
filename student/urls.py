from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_student, name="create-student"),
    path('list/', views.student_list, name="student-list"),
    path('search/', views.search_student, name="search-student"),

]
