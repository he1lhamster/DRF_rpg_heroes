from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response

from heroes.models import PCharacter
from heroes.serializers import PCSerializer
from rest_framework.views import APIView


class PCharacterAPIList(generics.ListCreateAPIView):
    queryset = PCharacter.objects.all()
    serializer_class = PCSerializer


class PCharacterAPIUpdate(generics.UpdateAPIView):
    queryset = PCharacter.objects.all()
    serializer_class = PCSerializer


class PCharacterAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PCharacter.objects.all()
    serializer_class = PCSerializer

# class PCharactersAPIView(APIView):
#     def get(self, request):
#         pc = PCharacter.objects.all()
#         return Response({'posts': PCSerializer(pc, many=True).data})
#
#     def post(self, request):
#         serializer = PCSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = PCharacter.objects.get(pk=pk)
#         except:
#             return Response({"error": "Objects does not exist"})
#
#         serializer = PCSerializer(data=request.data, instance=instance)
#         serializer.is_valid()
#         serializer.save()
#         return Response({"post": "serializer.data"})

# class PCharactersAPIView(generics.ListAPIView):
#     queryset = PCharacter.objects.all()
#     serializer_class = PCSerializer
