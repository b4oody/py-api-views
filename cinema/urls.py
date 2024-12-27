from django.urls import path

from cinema.views import (
    GenreList,
    GenreDetail,
)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genres-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genres-detail"),


]

app_name = "cinema"
