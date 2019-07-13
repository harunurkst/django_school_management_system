from rest_framework import serializers
from student.models import StudentInfo


class ResultSerializer(serializers.Serializer):
    board = serializers.CharField(max_length=10)
    roll = serializers.IntegerField()


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'
