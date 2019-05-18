from django.db import models


class StudentShiftInfo(models.Model):
    shift_name = models.CharField(max_length=50)

    def __str__(self):
        return self.shift_name

class StudentClassInfo(models.Model):
    class_name = models.CharField(max_length=50)
    class_short_form = models.CharField(max_length=10)

    def __str__(self):
        return self.class_name


class StudentInfo(models.Model):
    roll = models.IntegerField()
    fathers_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(choices=gender_choice, max_length=6)

    def __str__(self):
        return self.name


class StudentDetailInfo(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    std_class = models.ForeignKey(StudentClassInfo, on_delete=models.CASCADE)
    std_shift = models.ForeignKey(StudentShiftInfo, on_delete=models.CASCADE)
    std_section = models.CharField(max_length=50)
    session = models.IntegerField()

    def __str__(self):
        return self.student.name








