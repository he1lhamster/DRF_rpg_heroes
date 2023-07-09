from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from heroes.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/drf-auth/", include("rest_framework.urls")),
    path("api/v1/pcharacters/", PCharacterAPIList.as_view()),
    path("api/v1/pcharacters/<int:pk>/", PCharacterAPIUpdate.as_view()),
    path("api/v1/pcharactersdelete/<int:pk>", PCharacterAPIDestroy.as_view()),

    path("api/v1/auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),

    path("api/v1/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("api/v1/token/verify/", TokenVerifyView.as_view(), name='token_verify'),

]
