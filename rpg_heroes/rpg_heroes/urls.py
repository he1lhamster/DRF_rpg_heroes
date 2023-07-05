from django.contrib import admin
from django.urls import path, include

from heroes.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'pcharacters', PCharacterViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    # path("api/v1/pcharacterslist/", PCharacterViewSet.as_view({'get': 'list'})),
    # path("api/v1/pcharacterslist/<int:pk>/", PCharacterViewSet.as_view({'put': 'update'})),

]
