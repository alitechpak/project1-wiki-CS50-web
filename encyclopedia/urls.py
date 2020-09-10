from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:md_entry>", views.topic, name="topic"),
    path("/", views.search, name="search"),
    path("create", views.create, name="create"),
]
