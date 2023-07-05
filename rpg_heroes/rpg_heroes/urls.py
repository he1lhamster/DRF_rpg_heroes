from django.contrib import admin
from django.urls import path

from heroes.views import PCharactersAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/pcharacterslist/", PCharactersAPIView.as_view()),
    path("api/v1/pcharacterslist/<int:pk>/", PCharactersAPIView.as_view()),

]
