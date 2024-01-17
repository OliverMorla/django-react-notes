from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Note
from .serializers import NoteSerializer


# Create your views here.
def index(request):
    return JsonResponse({"message": "Django server is running!"}, safe=False)


@api_view(["GET"])
def getNotes(request):
    Notes = [
        {"id": "1", "title": "Note 1", "body": "This is note 1"},
        {"id": "2", "title": "Note 2", "body": "This is note 2"},
    ]

    return Response(Notes)


@api_view(["GET"])
def getNotesFromDB(request: HttpRequest):
    # request.method == "GET"
    
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getNote(request, pk):
    # param = request.GET.get("id")

    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def createNote(request):
    data = request.data
    notes = Note.objects.create(title=data["title"], body=data["body"])
    return JsonResponse({"message": "Django server is running!"}, safe=False)


@api_view(["PUT"])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()

    return Response("Note was deleted!")


class NoteView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
