from django.db import models
from django.contrib.auth.models import User 


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DESIGNATIONS = (
        ('accounts', 'Accounts'),

    )
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    designation = models.CharField(max_length=50, choices=DESIGNATIONS)

    def __str__(self):
        return self.name