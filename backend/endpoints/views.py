# Import necessary Django modules and components.
from django.shortcuts import (
    render,
)  # Used for rendering templates, not used in your code.
from django.http import (
    HttpResponse,
    JsonResponse,
    HttpRequest,
)  # HttpResponse is not used. JsonResponse is used to send JSON responses. HttpRequest is a class to represent HTTP requests.
from rest_framework import (
    generics,
    status,
)  # Used for class-based views in Django Rest Framework.
from rest_framework.response import (
    Response,
)  # Used to return responses in Django Rest Framework views.
from rest_framework.decorators import (
    api_view,
)  # Decorator to define API views with Django Rest Framework.

# Importing the model and serializer you created.
from .models import (
    Note,
    User,
)  # Import the Note model from the models.py in the same directory.
from .serializers import (
    NoteSerializer,
    UserSerializer,
)  # Import the NoteSerializer from serializers.py.


# Define the index view.
def index(request):
    # Return a JSON response with a message, not using Django's 'safe' parameter as it's not a dictionary.
    return render(request, "endpoints/index.html")


# Define a view for getting routes, decorated with @api_view to specify that it's an API view.
@api_view(["GET"])
def getRoutes(request: HttpRequest):
    # Define a dictionary of routes.
    routes = [
        {
            "Endpoint": "/notes",
            "method": "GET",
            "body": None,
            "description": "Returns an array of notes.",
        },
        {
            "Endpoint": "/notes/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single note object.",
        },
        {
            "Endpoint": "/notes/create",
            "method": "POST",
            "body": {"body": ""},
            "description": "Creates a new note with data sent in post request.",
        },
        {
            "Endpoint": "/notes/id/update",
            "method": "PUT",
            "body": {"body": ""},
            "description": "Updates an existing note with data sent in post request.",
        },
        {
            "Endpoint": "/notes/id/delete",
            "method": "DELETE",
            "body": None,
            "description": "Deletes an existing note.",
        },
    ]

    # Return the routes dictionary as a JSON response.
    return Response(routes, status=status.HTTP_200_OK)


# Define a view for getting notes from the database.
@api_view(["GET", "POST"])
def getNotes(request: HttpRequest):
    if request.method == "GET":
        # Get all note objects from the database.
        notes = Note.objects.all()
        # Serialize the note objects.
        serializer = NoteSerializer(notes, many=True)
        # Return the serialized data.
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = NoteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Define a view for getting a specific note based on its primary key (pk).
@api_view(["GET", "PUT", "DELETE"])
def getNote(request: HttpRequest, pk):
    # Check the request method
    if request.method == "GET":
        # Retrieve the note from the database using the provided pk.
        notes = Note.objects.get(id=pk)
        # Serialize the note object.
        serializer = NoteSerializer(notes, many=False)
        # Return the serialized data.
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        # Get the data from the request.
        data = request.data
        # Retrieve the note to be updated using the provided pk.
        note = Note.objects.get(id=pk)
        # Create a serializer instance with the note object and new data.
        serializer = NoteSerializer(instance=note, data=data)

        # Check if the new data is valid.
        if serializer.is_valid():
            # Save the updated note.
            serializer.save()

        # Return the updated data.
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == "DELETE":
        # Retrieve the note to be deleted using the provided pk.
        note = Note.objects.get(id=pk)
        # Delete the note.
        note.delete()

        # Return a response confirming deletion.
        return Response("Note was deleted!", status=status.HTTP_204_NO_CONTENT)


# Define a view for getting notes from the database using Django Rest Framework's generic views.
class NotesView(generics.ListCreateAPIView):
    # Set the queryset to all Note objects.
    queryset = Note.objects.all()
    # Specify the serializer class to be used.
    serializer_class = NoteSerializer


class NoteView(generics.RetrieveUpdateDestroyAPIView):
    # Set the queryset to all Note objects.
    queryset = Note.objects.all()
    # Specify the serializer class to be used.
    serializer_class = NoteSerializer


# Define a view for getting users from the database using Django Rest Framework's generic views.
class UsersView(generics.ListCreateAPIView):
    # Set the queryset to all User objects.
    queryset = User.objects.all()
    # Specify the serializer class to be used.
    serializer_class = UserSerializer


class UserView(generics.RetrieveUpdateDestroyAPIView):
    # Set the queryset to all User objects.
    queryset = User.objects.all()
    # Specify the serializer class to be used.
    serializer_class = UserSerializer
