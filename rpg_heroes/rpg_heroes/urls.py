from django.contrib import admin
from django.urls import path, include, re_path

from heroes.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/drf-auth/", include("rest_framework.urls")),
    path("api/v1/pcharacters/", PCharacterAPIList.as_view()),
    path("api/v1/pcharacters/<int:pk>/", PCharacterAPIUpdate.as_view()),
    path("api/v1/pcharactersdelete/<int:pk>", PCharacterAPIDestroy.as_view()),

    path("api/v1/auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
]
