from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from heroes.models import PCharacter


class PCSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_cast_spells = serializers.BooleanField(default=False)
    p_class_id = serializers.IntegerField()
    level = serializers.IntegerField()

    def create(self, validated_data):
        return PCharacter.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.level = validated_data.get("level", instance.level)
        instance.is_cast_spells = validated_data.get("is_cast_spells", instance.is_cast_spells)
        instance.p_class_id = validated_data.get("p_class_id", instance.p_class_id)
        instance.save()
        return instance


# def encode():
#     model = PCModel('Siila', 2)
#     model_sr = PCSerializer(model)
#     print(model_sr.data, sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
