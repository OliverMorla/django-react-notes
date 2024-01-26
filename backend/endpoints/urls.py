"""
URL configuration for notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import (
    index,
    getNotes,
    getNote,
    getRoutes,
    NotesView,
    NoteView,
    UsersView,
)

urlpatterns = [
    path("", index, name="index"),
    path("api/routes/", getRoutes, name="routes"),
    path("api/notes/", getNotes, name="notes"),
    path("api/note/<str:pk>/", getNote, name="note"),
    path("api/model-view/notes", NotesView.as_view(), name="notes"),
    path("api/model-view/note/<str:pk>", NoteView.as_view(), name="note"),
    path("api/model-view/users", UsersView.as_view(), name="users"),
]
