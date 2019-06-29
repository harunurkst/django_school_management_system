from rest_framework import serializers


class ResultSerializer(serializers.Serializer):
    board = serializers.CharField(max_length=10)
    roll = serializers.IntegerField()

