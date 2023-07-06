from django.forms import model_to_dict
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.decorators import action
from heroes.models import PCharacter, PClass
from heroes.serializers import PCSerializer


class PCharacterViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = PCharacter.objects.all()
    serializer_class = PCSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return PCharacter.objects.all()[:3]
        return PCharacter.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def p_class(self, request, pk=None): # ulr += /p_class
        p_class = PClass.objects.get(pk=pk)
        return Response({'classes': p_class.name})

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
