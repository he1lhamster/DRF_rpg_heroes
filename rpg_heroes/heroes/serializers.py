from rest_framework import serializers
from heroes.models import PCharacter


class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PCharacter
        fields = "__all__"
