from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from student.models import Attendance
from .serializers import ResultSerializer, StudentInfoSerializer
from student.models import Result, StudentInfo


class StudentInfoView(APIView):
    def get(self, request):
        students = StudentInfo.objects.all()
        std_serializer = StudentInfoSerializer(students, many=True)
        return Response({'status': std_serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentInfoSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        return Response({'status': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def std_attendance(request, std_cls, std_roll):
    try:
        Attendance.objects.create_attendance(std_cls, std_roll)
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST)


class StudentAttendancec(APIView):
    def get(self, request, std_cls, std_roll):
        try:
            Attendance.objects.create_attendance(std_cls, std_roll)
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST)


class ResultView(APIView):
    def post(self, request):
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            board = serializer.validated_data["board"]
            roll = serializer.validated_data["roll"]

            result_obj = Result.objects.get(board=board, roll=roll)
            
            return Response({'result': result_obj.gpa}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)