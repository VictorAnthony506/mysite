from rest_framework import serializers
from render.models import Operation
from django.db.models import F


class OperationSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    # slackUsername = serializers.CharField(default="anthonyvictor385", max_length=255, read_only=True)
    # result = serializers.FloatField(default=0)
    operation_type = serializers.CharField(max_length=255)
    x = serializers.IntegerField()
    y = serializers.IntegerField()
    

    
    def create(self, validated_data):
        return Operation.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # instance.slackUsername = validated_data.get("slackUsername", instance.slack_username)
        instance.x = validated_data.get("x", instance.x) 
        instance.y = validated_data.get("y", instance.y)
        instance.operation_type = validated_data.get("operation_type", instance.operation_type)
        instance.save()
        return instance