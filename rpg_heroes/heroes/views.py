from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import GenericViewSet, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
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
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)


class PCharacterAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = PCharacter.objects.all()
    serializer_class = PCSerializer
    permission_classes = (IsAdminOrReadOnly, )