from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.response import Response

from heroes.models import PCharacter
from heroes.serializers import PCSerializer
from rest_framework.views import APIView


class PCharacterViewSet(viewsets.ModelViewSet):
    queryset = PCharacter.objects.all()
    serializer_class = PCSerializer

#
# class PCharacterAPIList(generics.ListCreateAPIView):
#     queryset = PCharacter.objects.all()
#     serializer_class = PCSerializer
#
#
# class PCharacterAPIUpdate(generics.UpdateAPIView):
#     queryset = PCharacter.objects.all()
#     serializer_class = PCSerializer
#
#
# class PCharacterAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PCharacter.objects.all()
#     serializer_class = PCSerializer

# class PCharactersAPIView(generics.ListAPIView):
#     queryset = PCharacter.objects.all()
#     serializer_class = PCSerializer
