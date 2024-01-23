from rest_framework import serializers
from .models import Note, User


# Define the serializer class. This is similar to defining forms in Django.
class NoteSerializer(serializers.ModelSerializer):
    # Define the model and fields to serialize.
    class Meta:
        model = Note
        fields = "__all__"  # This is a list of strings, so you can use "__all__" to serialize all fields.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"