from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics

from .models import User
from .serializers import UserSerializer


# Create your views here.
def index(request):
    return JsonResponse({"message": "Django server is running!"}, safe=False)


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
