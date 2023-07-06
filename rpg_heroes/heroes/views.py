from django.forms import model_to_dict
from rest_framework.viewsets import GenericViewSet, generics
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from heroes.models import PCharacter, PClass
from heroes.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from heroes.serializers import PCSerializer


class PCharacterAPIList(generics.ListCreateAPIView):
    queryset = PCharacter.objects.all()
    serializer_class = PCSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PCharacterAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = PCharacter.objects.all()
    serializer_class = PCSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class PCharacterAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = PCharacter.objects.all()
    serializer_class = PCSerializer
    permission_classes = (IsAdminOrReadOnly, )


# class PCharacterViewSet(mixins.CreateModelMixin,
#                         mixins.RetrieveModelMixin,
#                         mixins.UpdateModelMixin,
#                         mixins.ListModelMixin,
#                         GenericViewSet):
#     queryset = PCharacter.objects.all()
#     serializer_class = PCSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return PCharacter.objects.all()[:3]
#         return PCharacter.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True)
#     def p_class(self, request, pk=None): # ulr += /p_class
#         p_class = PClass.objects.get(pk=pk)
#         return Response({'classes': p_class.name})

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
