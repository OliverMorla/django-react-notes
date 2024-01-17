from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        # fields = ("title", "body", "...")
        # fields = '__all__' # if you want to serialize all fields
