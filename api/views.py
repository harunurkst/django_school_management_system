from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from student.models import Attendance


@api_view()
def std_attendance(request, std_cls, std_roll):
    try:
        Attendance.objects.create_attendance(std_cls, std_roll)
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST)
