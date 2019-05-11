from django.db import models


class TeacherInfo(models.Model):
    name = models.CharField(max_length=50, unique=True)
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(choices=gender_choice, max_length=6)
    phone_number = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.name
