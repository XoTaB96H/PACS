from rest_framework import serializers

class CheckAccessSerializer(serializers.Serializer):
    credential_value = serializers.CharField(required=True)
    device_id = serializers.IntegerField(required=True)
