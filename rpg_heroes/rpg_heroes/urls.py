from django.contrib import admin
from django.urls import path

from heroes.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/pcharacterslist/", PCharacterAPIList.as_view()),
    path("api/v1/pcharacterslist/<int:pk>/", PCharacterAPIUpdate.as_view()),
    path("api/v1/pcharacterdetail/<int:pk>/", PCharacterAPIDetailView.as_view()),

]
