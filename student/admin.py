from django.contrib import admin
from .models import StudentInfo, StudentDetailInfo, StudentClassInfo, StudentShiftInfo


admin.site.register(StudentInfo)
admin.site.register(StudentDetailInfo)
admin.site.register(StudentClassInfo)
admin.site.register(StudentShiftInfo)


