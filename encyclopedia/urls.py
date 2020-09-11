from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:md_entry>", views.topic, name="topic"),
    path("/", views.search, name="search"),
    path("create", views.create, name="create"),
    path("edit/<str:md_entry>", views.edit, name="editPage"),
    path("random", views.randomPage, name="randomPage"),
]
