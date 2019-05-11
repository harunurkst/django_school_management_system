from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_teacher, name="create-teacher"),
    path('list/', views.teacher_list, name="teacher-list"),
    path('edit/<int:teacher_id>', views.edit_teacher, name="edit-teacher"),
    path('delete/<int:teacher_id>', views.delete_teacher, name="delete-teacher"),

]
