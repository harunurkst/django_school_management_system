from django.db import models


class StudentInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(choices=gender_choice, max_length=6)

    def __str__(self):
        return self.name




