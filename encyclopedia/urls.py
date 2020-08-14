from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.randomP, name="random"),
    path("wiki/<str:title>", views.entryPage, name="entry"),
    path("create", views.createPage, name="create"),
    path("edit/<str:title>", views.editPage, name="edit"),
]
