from rest_framework import serializers
from heroes.models import PCharacter


class PCSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = PCharacter
        fields = "__all__"
